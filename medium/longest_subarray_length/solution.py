# Problem Statement: https://www.geeksforgeeks.org/problems/longest-subarray-length--202010/1

class Solution:
    def longestSubarray(self, arr):
        # code here
        stack = []
        nge_left = [-1] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                nge_left[stack.pop()] = i
            stack.append(i)

        stack = []
        nge_right = [len(arr)] * len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] < arr[i]:
                nge_right[stack.pop()] = i
            stack.append(i)

        maxi = 0
        for i in range(len(arr)):
            l = nge_right[i] - nge_left[i] - 1
            v = arr[i]
            if v <= l:
                maxi = max(maxi, l)
        return maxi
