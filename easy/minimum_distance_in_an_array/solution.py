# Problem Statement: https://www.geeksforgeeks.org/problems/minimum-distance-between-two-numbers/1


class Solution:
    def minDist(self, arr, n, x, y):
        # xi and yi store the indexs of x and y occurances
        xi, yi = [], []
        found_x, found_y = False, False

        for i in range(n):
            if arr[i] == x:
                found_x = True
                xi.append(i)
            if arr[i] == y:
                found_y = True
                yi.append(i)

        # Return -1 if either x or y not found
        if not found_x or not found_y:
            return -1

        # Check min dist by checking all possible index differences
        res = n+1
        for i in xi:
            for j in yi:
                res = min(res, abs(i-j))

        return res


# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x, y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))


# } Driver Code Ends
