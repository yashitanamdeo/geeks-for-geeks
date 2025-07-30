# Problem Statement: https://practice.geeksforgeeks.org/problems/find-nth-element-of-spiral-matrix/1

# User function Template for python3

class Solution:
    def findK(self, a, n, m, k):
        # Write Your Code here

        traversed = []
        top, bottom, left, right = 0, n-1, 0, m-1

        # While its possible to move further down and to right
        while top <= bottom and left <= right:
            for i in range(left, right+1):
                # Adding the ith element of the topmost row
                traversed.append(a[top][i])
            # As first row is traversed increment the top
            top += 1

            for i in range(top, bottom+1):
                # Adding the rightmost value  of ith  row from top to bottom
                traversed.append(a[i][right])
            # Incrementing right as all the rightmost values have been traversed
            right -= 1

            for i in range(right, left-1, -1):
                # Adding the ith element of the bottommost row
                traversed.append(a[bottom][i])
            # Decrementing the bottom value as the last row is already traversed
            bottom -= 1

            for i in range(bottom, top-1, -1):
                # # Adding the leftmost value  of ith  row from top to bottom
                traversed.append(a[i][left])
            left += 1
        return traversed[k-1]


# {
 # Driver Code Starts

# Initial Template for Python 3

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    ob = Solution()
    print(ob.findK(a, n, m, k))

# } Driver Code Ends
