# Problem Statement: https://www.geeksforgeeks.org/problems/node-at-distance/1

#User function Template for python3

'''
@input - 
node - root node of given tree
k = distance of nodes required 

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    #Function to return count of nodes at a given distance from leaf nodes.
    def dfs(self,root,stack,k,vis):
        if root:
            stack.append(root)
            if not root.left and not root.right:
                n=len(stack)
                if n>k and (stack[-k-1] not in vis):
                    vis.add(stack[-k-1])
            self.dfs(root.left,stack,k,vis)
            self.dfs(root.right,stack,k,vis)
            stack.pop()
    
    def printKDistantfromLeaf(self, root, k):
        vis=set()
        self.dfs(root,[],k,vis)
        return len(vis)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

MAX_HEIGHT = 100000
c=0
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


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        k = int(input())
        ob = Solution()
        print(ob.printKDistantfromLeaf(root, k))

# } Driver Code Ends