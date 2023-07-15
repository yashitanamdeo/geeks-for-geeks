# Problem Statement: https://practice.geeksforgeeks.org/problems/delete-middle-element-of-a-stack/1

#User function Template for python3

class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid_util(self, s, sizeOfStack, current):
        
        #if current pointer is half of the size of stack then we 
        #are accessing the middle element of stack.
        if(current==sizeOfStack//2):
            s.pop()
            return
        
        #storing the top element in a variable and popping it.
        x = s.pop()
        current+=1
        
        #calling the function recursively.
        self.deleteMid_util(s,sizeOfStack,current)
        
        #pushing the elements (except middle element) back 
        #into stack after recursion calls.
        s.append(x)

    def deleteMid(self, s, sizeOfStack):
        self.deleteMid_util(s, sizeOfStack, 0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
sys.setrecursionlimit(10**8)

def main():
    t=int(input())
    while(t>0):
        sizeOfStack=int(input())
        myStack=[int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack,sizeOfStack)
        while(len(myStack)>0):
            print(myStack[-1],end=" ")
            myStack.pop()
        print()
        t-=1


if __name__=="__main__":
    main()
    
    
# } Driver Code Ends