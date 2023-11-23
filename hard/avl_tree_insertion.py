# Problem Statement: https://www.geeksforgeeks.org/problems/avl-tree-insertion/1

#User function Template for python3

''' structure of tree node:

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''
class Solution:
    def getHeight(self, node):
        return 0 if not node else node.height

    def getBalance(self, root):
        return 0 if not root else (self.getHeight(root.left) - self.getHeight(root.right))

    def leftRotate(self, root):
        y = root.right
        t2 = y.left
        root.right = t2
        y.left = root
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, root):
        y = root.left
        t2 = y.right
        root.left = t2
        y.right = root
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def insertToAVL(self, root, key):
        # add key to AVL (if it is not present already)
        # return root node
        if not root:
            root = Node(key)
            return root
        elif key == root.data:
            return root
        elif key < root.data:
            root.left = self.insertToAVL(root.left, key)
        else:
            root.right = self.insertToAVL(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        b = self.getBalance(root)
        # L-L case
        if b > 1 and key < root.left.data:
            return self.rightRotate(root)
        # R-R case
        if b < -1 and key > root.right.data:
            return self.leftRotate(root)
        # L-R case
        if b > 1 and key > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # R-L case
        if b < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

def isBST(n, lower, upper):
    if not n:
        return True
    
    if n.data <= lower or n.data >= upper:
        return False
    
    return isBST(n.left, lower, n.data) and isBST(n.right, n.data, upper)

def isBalanced(n):
    if not n:
        return (0,True)
    
    lHeight, l = isBalanced(n.left)
    rHeight, r = isBalanced(n.right)
    
    if abs( lHeight - rHeight ) > 1:
        return (0, False)
    
    return ( 1 + max( lHeight,rHeight  ) , l and r )

def isBalancedBST(root):
    if not isBST(root, -1000000000, 1000000000):
        print("BST voilated, inorder traversal :", end=' ')
    
    elif not isBalanced(root)[1]:
        print("Unbalanced BST, inorder traversal :", end=' ')
    
    else:
        return True
    
    return False

def printInorder(n):
    if not n:
        return
    printInorder(n.left)
    print(n.data, end=' ')
    printInorder(n.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        ip = [ int(x) for x in input().strip().split() ]
        
        root = None
        
        for i in range(n):
            root = Solution().insertToAVL( root, ip[i] )
            
            if not isBalancedBST( root ):
                break
        
        printInorder(root)
        print()

# } Driver Code Ends