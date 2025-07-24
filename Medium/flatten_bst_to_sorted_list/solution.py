# Problem Statement: https://www.geeksforgeeks.org/problems/flatten-bst-to-sorted-list--111950/1

#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

import sys
sys.setrecursionlimit(10000)
class Solution:
    def inorder(self,root,prev):
        if root:
            self.inorder(root.left,prev)
            root.left=None
            prev[0].right=root
            prev[0]=root
            self.inorder(root.right,prev)
    def flattenBST(self, root):
        temp=Node(0)
        self.inorder(root,[temp])
        return temp.right


#{ 
 # Driver Code Starts

#Initial Template for Python 3

from queue import Queue

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def newNode(key):
    node = Node(key)
    return node

def buildTree(s):
    if len(s) == 0 or s[0] == 'N':
        return None

    ip = s.split()
    root = newNode(int(ip[0]))
    q = Queue()
    q.put(root)

    i = 1
    while not q.empty() and i < len(ip):
        currNode = q.get()

        currVal = ip[i]
        if currVal != "N":
            currNode.left = newNode(int(currVal))
            q.put(currNode.left)

        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]
        if currVal != "N":
            currNode.right = newNode(int(currVal))
            q.put(currNode.right)

        i += 1

    return root


def printList(head):
    # if head==None:
    #     return
    # print(head.data, end=" ")
    # printList(head.left)
    # printList(head.right)
    while head:
        if head.left:
            print(-1,end=" ")
        print(head.data, end=" ")
        head = head.right
        
    print()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        ans = ob.flattenBST(root)
        printList(ans)
        # print()

# } Driver Code Ends