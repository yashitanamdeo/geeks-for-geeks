# Problem Statement: https://practice.geeksforgeeks.org/problems/e2d156755ca4e0a9b9abf5680191d4b06e52b1a8/1

#{
# Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def goodStones(self, n, arr) -> int:

        visited = [0]*n

        def dfs(i):

            nonlocal arr, visited, n
            if i < 0 or i >= n:
                return True

            if visited[i] > 0:
                return visited[i] == 2

            visited[i] = 1
            if dfs(i+arr[i]):
                visited[i] = 2
                return True
            return False

        return sum(dfs(i) for i in range(n))

#{
 # Driver Code Starts.


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        obj = Solution()
        print(obj.goodStones(n, arr))

# } Driver Code Ends
