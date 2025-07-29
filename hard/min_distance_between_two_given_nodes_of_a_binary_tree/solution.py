# Problem Statement: https://www.geeksforgeeks.org/problems/min-distance-between-two-given-nodes-of-a-binary-tree/1

#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def findDist(self, root, node_val_1, node_val_2):
        def distance_to_node(node, target):
            if not node:
                return -1
            if node.data == target:
                return 0

            left_distance = distance_to_node(node.left, target)
            right_distance = distance_to_node(node.right, target)

            if left_distance >= 0:
                return left_distance + 1
            if right_distance >= 0:
                return right_distance + 1

            return -1

        def lowest_common_ancestor(node, node_val_1, node_val_2):
            if not node:
                return None
            if node.data == node_val_1 or node.data == node_val_2:
                return node

            left_lca = lowest_common_ancestor(node.left, node_val_1, node_val_2)
            right_lca = lowest_common_ancestor(node.right, node_val_1, node_val_2)

            if left_lca and right_lca:
                return node
            return left_lca if left_lca else right_lca

        lca_node = lowest_common_ancestor(root, node_val_1, node_val_2)
        return distance_to_node(lca_node, node_val_1) + distance_to_node(lca_node, node_val_2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

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
        a, b=map(int, input().split())
        ob = Solution()
        print(ob.findDist(root, a, b))

# } Driver Code Ends