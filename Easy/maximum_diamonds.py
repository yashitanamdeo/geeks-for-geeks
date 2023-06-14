# Problem Statement: https://practice.geeksforgeeks.org/problems/chinky-and-diamonds3340/1

# User function Template for python3

from heapq import heapify, heappushpop


class Solution:
    def maxDiamonds(self, A, N, K):
        heap = [-diamonds for diamonds in A]
        heapify(heap)

        gain = 0
        for i in range(K):
            diamonds = heap[0]
            gain -= diamonds
            heappushpop(heap, -((-diamonds) // 2))
        return gain


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))

        ob = Solution()
        print(ob.maxDiamonds(A, N, K))
# } Driver Code Ends
