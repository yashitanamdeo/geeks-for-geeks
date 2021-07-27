#User function Template for python3

class Solution:
    def snowball(self, N, weights):
        #code here
        sum = 0
        for i in weights:
            sum += i
        return sum

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        weights = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.snowball(N, weights))

# } Driver Code Ends