# Problem Statement: https://practice.geeksforgeeks.org/problems/task-scheduler/1

# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3

class Solution:
    def leastInterval(self, N, K, tasks):
        # Code here
        freq = {}

        for i in tasks:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        max_freq = max(freq.values())

        ans = (K + 1) * (max_freq - 1)

        for i in freq.values():
            if max_freq == i:
                ans += 1

        return max(ans, N)


# {
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, K = list(map(int, input().split()))
        tasks = input().split()
        ob = Solution()
        res = ob.leastInterval(N, K, tasks)
        print(res)
# } Driver Code Ends
