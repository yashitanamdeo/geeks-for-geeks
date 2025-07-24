# Problem Statement: https://practice.geeksforgeeks.org/problems/chicks-in-a-zoo1159/1

# User function Template for python3


total = {1: 1}
chicks = {1: 1}

for i in range(2, 36):
    if i > 6:
        chick = total[i-1]-chicks[i-6]
    else:
        chick = total[i-1]
    total[i] = chick+chick*2
    chicks[i] = chick*2


class Solution:
    def NoOfChicks(self, N):
        return total[N]


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        obj = Solution()
        ans = obj.NoOfChicks(N)
        print(ans)

# } Driver Code Ends
