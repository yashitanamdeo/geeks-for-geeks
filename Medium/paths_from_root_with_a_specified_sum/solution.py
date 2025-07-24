# Problem Statement: https://www.geeksforgeeks.org/problems/paths-from-root-with-a-specified-sum/1

#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
'''

from collections import deque

class Solution:
    def printPaths(self, root, target_sum):
        if not root:
            return []

        # Using a queue to perform level-order traversal
        queue, result = deque(), []

        # Initial state: [current_node, current_sum, current_route]
        queue.append([root, root.data, [root.data]])

        while queue:
            current_node, current_sum, current_route = queue.popleft()

            # Check if the current path satisfies the target_sum
            if current_sum == target_sum:
                result.append(current_route[:])

            # Explore left child
            if current_node.left:
                left_child = current_node.left
                queue.append([left_child, current_sum + left_child.data, current_route + [left_child.data]])

            # Explore right child
            if current_node.right:
                right_child = current_node.right
                queue.append([right_child, current_sum + right_child.data, current_route + [right_child.data]])

        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

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
    test_cases = int(input())
    for cases in range(test_cases):
        sum=int(input())
        s=input()
        root = buildTree(s)
        ob = Solution()
        ans = ob.printPaths(root, sum)
        ans = sorted(ans)
        
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                print(ans[i][j], end=" ")
                
            print()
            
# } Driver Code Ends