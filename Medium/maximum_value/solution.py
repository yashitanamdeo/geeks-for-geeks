# Problem Statement: https://practice.geeksforgeeks.org/problems/ec277982aea7239b550b28421e00acbb1ea03d2c/1

# {
# Driver Code Starts
# Initial Template for Python 3


from collections import deque
import sys
sys.setrecursionlimit(50000)
# Tree Node


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if(len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size+1

    # Starting from the second element
    i = 1
    while(size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size-1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if(currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size+1
        # For the right child
        i = i+1
        if(i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if(currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size+1
        i = i+1
    return root


# } Driver Code Ends
# User function Template for python3
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


class Solution:
    def maximumValue(self, node):
        # code here
        ans = []
        m = -1
        q = deque([node, None])
        while True:
            x = q.popleft()
            if x:
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)

                if x.data > m:
                    m = x.data
            else:
                ans.append(m)
                m = -1
                if q:
                    q.append(None)
                else:
                    return ans


# {
 # Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        obj = Solution()
        ans = obj.maximumValue(root)
        for i in ans:
            print(i, end=' ')
        print()

# } Driver Code Ends
