# Problem Statement: https://practice.geeksforgeeks.org/problems/median-of-bst/1

#User function Template for python3

def inorder(root):
    if root:
        return 1+inorder(root.left)+inorder(root.right)
    return 0

def kthSmallest(root,k):
    if root:
        stack=[]
        node=root
        while True:
            while node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            k-=1
            if k==0:
                return node.data
            node=node.right

def findMedian(root):
    n=inorder(root)
    if n%2==0:
        t1=kthSmallest(root,n//2)
        t2=kthSmallest(root,(n//2)+1)
        return (t1+t2)//2 if (t1+t2)%2==0 else (t1+t2)/2
    else:
        return kthSmallest(root,(n+1)//2)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        s=input()
        root=buildTree(s)
        print(findMedian(root))

# } Driver Code Ends
