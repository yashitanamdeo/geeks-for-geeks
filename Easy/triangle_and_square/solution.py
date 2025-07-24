# Problem Statement: https://practice.geeksforgeeks.org/problems/3f48d387900a38bd9fd0594b93f9f4f97f5ada8a1644/1

#User function Template for python3

class Solution:
    def countShare(self,B):
        #code here
        if(B%2 != 0):B-=1
        return  int((((B**2)/2)-B)//4)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        b=int(input().strip())
        obj=Solution()
        print(obj.countShare(b))
        
# } Driver Code Ends