# Problem Statement: https://practice.geeksforgeeks.org/problems/maximum-sum-of-non-adjacent-nodes/1#

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
    def helper(self,node,InEx):
        if node == None:
            return
        L = [0] * 2
        R = [0] * 2
        
        LeftSub = self.helper(node.left, L)
        RightSub = self.helper(node.right, R)
        
        #inclusion
        InEx[0] = L[1] + R[1] + node.data
        
        #exlusion
        InEx[1] = max(L[1] + R[0], L[0] + R[1], L[0] + R[0], L[1] + R[1])
        
        '''
        Taking max of:
            Exclusion of Left + inclusion of right
            Exclusion of Right + inclusion of left
            Inclusion of Left + inclusion of right
            Exclusion of Left + Exclusion of right
        '''
    #Function to return the maximum sum of non-adjacent nodes.
    def getMaxSum(self,root):
        #code here
        if root == None:
            return 0
        InEx = [0]*2
        self.helper(root,InEx)
        
        return max(InEx[0], InEx[1])

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10**6)

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
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
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        print(ob.getMaxSum(root))
        
# } Driver Code Ends