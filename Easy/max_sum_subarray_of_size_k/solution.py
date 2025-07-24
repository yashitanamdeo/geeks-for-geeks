# Problem Statement: https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

# User function Template for python3
class Solution:
    def maximumSumSubarray(self, K, Arr, N):

        # initiazlization
        l_sum = sum(Arr[0:K])
        res = l_sum

        # main loop
        for i in range(K, N):
            l_sum = l_sum-Arr[i-K]+Arr[i]
            res = max(l_sum, res)

        return res


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N, K = input().split()
        N = int(N)
        K = int(K)
        Arr = list(map(int, input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K, Arr, N))
# } Driver Code Ends
