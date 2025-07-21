# Problem Statement: https://practice.geeksforgeeks.org/problems/break-a-number5913/1

#User function Template for python3


class Solution:
    def waysToBreakNumber(self, n):
        return (((n+1)*(n+2))//2)%((10**9)+7)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        print(ob.waysToBreakNumber(n))
        
# } Driver Code Ends