# Problem Statement: https://practice.geeksforgeeks.org/problems/shop-in-candy-store1145/1

#User function Template for python3

class Solution:

    def candyStore(self, candies,N,K):
        # code here
        candies.sort()
        len_ = N
        low = high = 0
        for i in range(len_):
            low = low+candies[i]
            high = high+candies[len_-i-1]
            N-=(1+K)
            if(N<=0):
                break
        return [low,high]
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        N,K = [int(x) for x in input().split()]
        candies = [int(x) for x in input().split()]

        solObj = Solution()

        print(*solObj.candyStore(candies,N,K))
# } Driver Code Ends