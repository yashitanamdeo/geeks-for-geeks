# Problem Statement: https://www.geeksforgeeks.org/problems/check-if-a-number-is-divisible-by-83957/1

#User function Template for python3

class Solution:
    def DivisibleByEight(self,s):
        #code here
        return 1 if int(s[-3:]) % 8 == 0 else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        print(ob.DivisibleByEight(S))
# } Driver Code Ends