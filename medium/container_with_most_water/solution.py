# Problem Statement: https://practice.geeksforgeeks.org/problems/container-with-most-water0535/1

# User function Template for python3


def maxArea(A, le):
    # code here
    i, j = 0, le-1
    ans = 0
    while i < j:
        height = min(A[i], A[j])
        ans = max(ans, height*(j-i))
        if A[i] < A[j]:
            i += 1
        elif A[i] > A[j]:
            j -= 1
        else:
            i += 1
            j -= 1
    return ans

# {
 # Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):

    n = int(input())
    l = list(map(int, input().split()))

    print(maxArea(l, n))


# } Driver Code Ends



class Solution2:
    def maxWater(self, arr):
        # code here
        left, right, max_area = 0, len(arr) - 1, 0
        while left < right:
            if arr[left] < arr[right]:
                area = arr[left] * (right - left)
                left += 1
            else:
                area = arr[right] * (right - left)
                right -= 1
            if area > max_area:
                max_area = area
        return max_area