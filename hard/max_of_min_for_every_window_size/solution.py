# Problem Statement: https://www.geeksforgeeks.org/problems/maximum-of-minimum-for-every-window-size3453/1

class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        left = [-1] * n
        right = [n] * n

        stack = []
        push, pop = stack.append, stack.pop

        # Step 1: Find previous smaller element
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                pop()
            left[i] = stack[-1] if stack else -1
            push(i)

        stack.clear()
        push, pop = stack.append, stack.pop

        # Step 2: Find next smaller element
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                pop()
            right[i] = stack[-1] if stack else n
            push(i)

        # Step 3: Store answers
        ans = [0] * (n + 1)
        for i in range(n):
            win = right[i] - left[i] - 1
            if arr[i] > ans[win]:
                ans[win] = arr[i]

        # Step 4: Fill remaining values
        for i in range(n - 1, 0, -1):
            if ans[i] < ans[i + 1]:
                ans[i] = ans[i + 1]

        return ans[1:]

