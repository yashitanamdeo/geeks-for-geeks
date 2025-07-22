# Problem Statement: https://www.geeksforgeeks.org/problems/smallest-positive-missing-number-1587115621/1

class Solution:
    def missingNumber(self, arr):
        n = len(arr)

        # Step 1: Replace non-positive and >n numbers with n+1
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = n + 1

        # Step 2: Mark present numbers
        for i in range(n):
            num = abs(arr[i])
            if 1 <= num <= n:
                arr[num - 1] = -abs(arr[num - 1])  # mark as negative

        # Step 3: Find the first missing positive
        for i in range(n):
            if arr[i] > 0:
                return i + 1

        return n + 1