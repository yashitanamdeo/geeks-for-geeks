# Problem Statement: https://www.geeksforgeeks.org/problems/sum-of-the-longest-bloodline-of-a-tree/1

#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
from collections import deque

class Solution:
    def sumOfLongRootToLeafPath(self, root):
        max_sum, max_length, queue = 0, 0, deque()
        queue.append([root, 1, root.data])  # [node, length, current_sum]
        
        while queue:
            node, length, current_sum = queue.popleft()
            
            # Check if leaf node
            if not node.left and not node.right:
                # Update max_sum and max_length if needed
                if (max_length < length) or (max_length == length and max_sum < current_sum):
                    max_length, max_sum = length, current_sum
                continue
            
            # Add left child to the queue
            if node.left:
                queue.append([node.left, length + 1, current_sum + node.left.data])
            
            # Add right child to the queue
            if node.right:
                queue.append([node.right, length + 1, current_sum + node.right.data])
        
        return max_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
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
    for cases in range(test_cases):
        s=input()
        root=buildTree(s)
        ob = Solution()
        res = ob.sumOfLongRootToLeafPath(root)
        print(res)
# } Driver Code Ends