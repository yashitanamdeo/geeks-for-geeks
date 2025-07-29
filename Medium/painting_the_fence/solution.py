# Problem Statement: https://www.geeksforgeeks.org/problems/painting-the-fence3727/1

#User function Template for python3

class Solution:
    def countWays(self,a,b):
        fi = b
        se = b**2
        if a == 1:
            return b
        sum1 = b**2
        for i in range(a-2):
            sum1 = ((fi + se)*(b-1)) % ((10**9)+7)
            fi = se
            se = sum1
        return sum1



#{ 
 # Driver Code Starts

#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    x=list(map(int,input().split()))
    n=x[0]
    k=x[1]
    ob = Solution()
    ans=ob.countWays(n,k)
    print(ans)

# } Driver Code Ends