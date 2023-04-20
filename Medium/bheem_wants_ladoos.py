# Problem Statement: https://practice.geeksforgeeks.org/problems/9b61b8efbb030aed799055f776629dbf1287fbae/1

'''
# node class:

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

from collections import deque

class Solution:
    def ladoos(self, root, home, k):
        if root is None: return 0
        
        if not root.left and not root.right:
            if root.data==home: return root.data
            return 0

        temp, q, pos, len1, node = {}, deque(), 0, 1, None
        q.append(root)
        
        while pos<len1:
            if q[pos].data==home:
                node=q[pos]
                break

            if q[pos].left:
                q.append(q[pos].left)
                temp[q[pos].left], len1 = q[pos], len1+1
            
            if q[pos].right:
                q.append(q[pos].right)
                temp[q[pos].right], len1 = q[pos], len1+1
            
            pos+=1

        q, sum1,temp1 = deque(), 0, set()
        q.append([node, 0])
        while q:
            node, k1 = q.popleft()
            sum1+=node.data
            temp1.add(node)
            if node.left and k1<k and node.left not in temp1:q.append([node.left, k1+1])
            if node.right and k1<k and node.right not in temp1:q.append([node.right, k1+1])
            if node in temp and k1<k and temp[node] not in temp1:q.append([temp[node], k1+1])
        return sum1




#{ 
 # Driver Code Starts
#driver code:
from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
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

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input()
        root=buildTree(line)
        line=input().strip().split()
        home=int(line[0])
        k=int(line[1])
        obj = Solution();
        print(obj.ladoos(root,home,k))


# } Driver Code Ends