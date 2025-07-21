# Problem Statement: https://practice.geeksforgeeks.org/problems/b64485d3994958cca8748991bb58668204b3e4c0/1

#User function Template for python3

class Solution():
    def maxWeightCell(self, N, Edge):
        weight = [0]*N
        for i in range(N):
            if Edge[i] != -1:
                weight[Edge[i]] += i
        mx = max(weight)
        return [i for i, n in enumerate(weight) if n == mx][-1]


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        Edge = [int(i) for i in input().split()]
        obj = Solution()
        ans = obj.maxWeightCell(N, Edge)
        print(ans)

# } Driver Code Ends
