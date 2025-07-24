# Problem Statement: https://www.geeksforgeeks.org/problems/path-with-minimum-effort/1


from typing import List

class Solution:
    def MinimumEffort(self, rows: int, columns: int, heights: List[List[int]]) -> int:
        def dfs(mid):
            stack = [(0, 0)]
            visited = set()
            while stack:
                x, y = stack.pop()
                if x == rows - 1 and y == columns - 1:
                    return True
                visited.add((x, y))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < columns and (nx, ny) not in visited and abs(heights[nx][ny] - heights[x][y]) <= mid:
                        stack.append((nx, ny))
            return False
        
        left, right, result = 0, int(1e6), float('inf')
        while left <= right:
            mid = (left + right) // 2
            if dfs(mid):
                result, right = mid, mid - 1
            else:
                left = mid + 1
        return result


#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        rows = int(input())

        columns = int(input())

        heights = IntMatrix().Input(rows, columns)

        obj = Solution()
        res = obj.MinimumEffort(rows, columns, heights)

        print(res)

# } Driver Code Ends