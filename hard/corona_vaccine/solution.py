# Problem Statement: https://practice.geeksforgeeks.org/problems/d1afdbd3d49e4e7e6f9d738606cd592f63e6b0f0/1

#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    number = 0
    def rec_count_vaccine(self, root):
        if root is None:
            return True, False
        
        L_got_vac, L_own_vac = self.rec_count_vaccine(root.left)
        R_got_vac, R_own_vac = self.rec_count_vaccine(root.right)
        
        root_got_vac = False
        root_own_vac = False
        
        if L_own_vac or R_own_vac:
            root_got_vac = True
            
        if L_got_vac == False or R_got_vac == False:
            root_own_vac = True
            root_got_vac = True
            self.number += 1
            
        return root_got_vac, root_own_vac
            
        
    def supplyVaccine(self, root):
        got_vac, own_vac = self.rec_count_vaccine(root)
        if got_vac == False:
            self.number += 1
        return self.number


#{ 
#  Driver Code Starts
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


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        print(ob.supplyVaccine(root))
        
# } Driver Code Ends