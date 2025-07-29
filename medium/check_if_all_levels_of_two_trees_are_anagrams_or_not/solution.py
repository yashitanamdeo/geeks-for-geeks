# Problem Statement: https://practice.geeksforgeeks.org/problems/check-if-all-levels-of-two-trees-are-anagrams-or-not/1

from typing import Optional
from collections import deque
"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    # Function to check if it is anagram
    def is_anagram(self,l1,l2):
        return sorted(l1) == sorted(l2)
    def areAnagrams(self, node1 : Optional['Node'], node2 : Optional['Node']) -> bool:
        # code here
        t1 = []
        t2 = []
        d1 = [node1]
        d2 = [node2]
        # Level Order Traversal of first Tree and storing it in t1 level wise
        while d1:
            temp = []
            for i in range(len(d1)):
                node = d1.pop(0)
                temp.append(node.data)
                if node.left:
                    d1.append(node.left)
                if node.right:
                    d1.append(node.right)
                    
            t1.append(temp)
        # Level Order Traversal of second Tree and storing it in t2 level wise
        while d2:
            temp = []
            for i in range(len(d2)):
                node = d2.pop(0)
                temp.append(node.data)
                if node.left:
                    d2.append(node.left)
                if node.right:
                    d2.append(node.right)
            t2.append(temp)
        # If they dont have same number of elements no use of checking for anagrams
        if len(t1) != len(t2):
            return 0
        for i in range(len(t1)):
            # If not anagram return 0
            if self.is_anagram(t1[i],t2[i]) == False:
                return 0
        return 1



#{ 
 # Driver Code Starts
class Node:
    def __init__(self,val):
        self.data=val
        self.right=None
        self.left=None

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

def inputTree():
    treeString=input().strip()
    root = buildTree(treeString)
    return root
def inorder(root):
    if (root == None):
       return
    inorder(root.left);
    print(root.data,end=" ")
    inorder(root.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        node1 = inputTree();
        
        
        node2 = inputTree();
        
        obj = Solution()
        res = obj.areAnagrams(node1, node2)
        
        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends