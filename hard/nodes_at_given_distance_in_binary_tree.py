# Problem Statement: https://practice.geeksforgeeks.org/problems/nodes-at-given-distance-in-binary-tree/1

# User function Template for python3

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
    def find_target(self, root, target):
        if root:
            left = self.find_target(root.left, target)
            if root.data == target:
                return root
            right = self.find_target(root.right, target)
            return left or right
        return None

    def find_parent(self, root):
        parent_of = dict()
        q = deque()
        q.append(root)
        while q:
            u = q.popleft()
            if u.left:
                q.append(u.left)
                parent_of[u.left] = u
            if u.right:
                q.append(u.right)
                parent_of[u.right] = u
        return parent_of

    def KDistanceNodes(self, root, target, k):
        parent_of = self.find_parent(root)
        target_pointer = self.find_target(root, target)
        visited = set()
        q = deque()
        q.append(target_pointer)
        visited.add(target_pointer.data)
        distance = 0
        while q:
            if distance == k:
                break
            for i in range(len(q)):
                u = q.popleft()
                if u.left and (u.left.data not in visited):
                    q.append(u.left)
                    visited.add(u.left.data)
                if u.right and (u.right.data not in visited):
                    q.append(u.right)
                    visited.add(u.right.data)
                if u in parent_of and (parent_of[u].data not in visited):
                    q.append(parent_of[u])
                    visited.add(parent_of[u].data)
            distance += 1
        result = [item.data for item in q]
        result.sort()
        return result


# {
 # Driver Code Starts
# Initial Template for Python 3


# Tree Node

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree


def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
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
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    x = Solution()
    t = int(input())
    for _ in range(t):
        line = input()
        target = int(input())
        k = int(input())

        root = buildTree(line)
        res = x.KDistanceNodes(root, target, k)

        for i in res:
            print(i, end=' ')
        print()

# } Driver Code Ends
