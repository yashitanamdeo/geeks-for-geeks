# Problem Statement: https://practice.geeksforgeeks.org/problems/d064cc0468a5c2bb7817ecd7c1bc59ce25e23613/1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def minSubtreeSumBST(self, target, root):
        def _solve(nd):# sum, isbst, total_nodes, min, max
            nonlocal ans
            if not nd: return 0, True, 0, inf, -inf
            Lsum, Lisbst, Lcnt, Lmin, Lmax = _solve(nd.left)
            Rsum, Risbst, Rcnt, Rmin, Rmax = _solve(nd.right)
            if not Lisbst or not Risbst or nd.data<=Lmax or nd.data>=Rmin: return (0, False, 0, inf, -inf)
            su = Lsum + Rsum + nd.data
            tot = Lcnt + Rcnt + 1
            if su == target:
                ans = min(ans, tot)
            if not nd.left: Lmin = nd.data
            if not nd.right: Rmax = nd.data
            return su, True, tot, Lmin, Rmax
            
        ans = inf
        _solve(root)
        return ans if ans != inf else -1
        

#{ 
 # Driver Code Starts.

#Initial Template for Python 3
from collections import defaultdict
from collections import deque
from sys import stdin, stdout
from math import inf
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
    test_cases = int(input())
    for _ in range (test_cases):
        target = int(input())
        N = input()
        root = buildTree(N)
        res = Solution().minSubtreeSumBST(target, root)
        print(res)
# } Driver Code Ends