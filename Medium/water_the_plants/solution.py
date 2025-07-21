# Problem Statement: https://www.geeksforgeeks.org/problems/water-the-plants--170646/1

# User function Template for python3

class Solution:
    def min_sprinklers(self, gallery, n):
        # code here
        intervals = sorted(
            [(i-g, i+g) for i, g in enumerate(gallery) if g != -1], reverse=True)
        reachable, best, res = 0, 0, 0

        while reachable < n:
            if intervals and intervals[-1][0] <= reachable:
                s, e = intervals.pop()
                best = max(best, e+1)
            elif best > reachable:
                reachable = best
                res += 1
            else:
                return -1
        return res


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        gallery = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.min_sprinklers(gallery, n))

# } Driver Code Ends
