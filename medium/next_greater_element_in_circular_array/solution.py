# Problem Statement: https://www.geeksforgeeks.org/problems/next-greater-element/1

class Solution:
    def nextGreater(self, arr):
        # code here
        narr = arr + arr
        res = [-1] * len(arr)
        stack = []
        for i in range(len(narr)):
            while stack and narr[stack[-1]] < narr[i]:
                ind = stack.pop()
                if ind < len(res):
                    res[ind] = narr[i]
            stack.append(i)
        return res