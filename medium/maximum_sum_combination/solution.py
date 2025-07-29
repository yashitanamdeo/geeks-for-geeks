# Problem Statement: https://practice.geeksforgeeks.org/problems/maximum-sum-combination/1

# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3
import heapq


class Solution:
    def maxCombinations(self, N, K, A, B):
        res = []
        A.sort(reverse=True)
        B.sort(reverse=True)
        pq = [(-(A[0]+B[0]), 0, 0)]
        visited = set((0, 0))
        while K:
            sum, i, j = heapq.heappop(pq)
            res.append(-sum)
            if i+1 < N and (i+1, j) not in visited:
                heapq.heappush(pq, (-(A[i+1]+B[j]), i+1, j))
                visited.add((i+1, j))
            if j+1 < N and (i, j+1) not in visited:
                heapq.heappush(pq, (-(A[i]+B[j+1]), i, j+1))
                visited.add((i, j+1))
            K -= 1
        return res


# {
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxCombinations(N, K, A, B)
        for val in res:
            print(val, end=' ')
        print()
# } Driver Code Ends
