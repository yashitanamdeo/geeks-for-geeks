# Problem Statement: https://www.geeksforgeeks.org/problems/trie-insert-and-search0651/1

#User function Template for python3

"""
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
"""

class Solution:
    #Function to insert string into TRIE.
    def insert(self, root, key):
        for e in key:
            ind=ord(e)-ord("a")
            if root.children[ind] is None:
                root.children[ind]=TrieNode()
            root=root.children[ind]
        root.isEndOfWord=True

    def search(self, root, key):
        for e in key:
            ind=ord(e)-ord("a")
            if root.children[ind] is None:
                return False
            root=root.children[ind]
        return root.isEndOfWord


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
        

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=input().strip().split()
        strs=input()
        
        t=Trie()
        ob = Solution()
        
        for s in arr:
            ob.insert(t.root,s)
        
        if ob.search(t.root,strs):
            print(1)
        else:
            print(0)
# } Driver Code Ends