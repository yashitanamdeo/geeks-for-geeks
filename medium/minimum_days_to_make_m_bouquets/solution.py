# Problem Statement: https://www.geeksforgeeks.org/problems/minimum-days-to-make-m-bouquets/1

class Solution:
    def minDaysBloom(self, arr, k, m):
        n = len(arr)
        if m * k > n:
            return -1  # Not enough flowers

        def canMake(day):
            bouquets = 0
            flowers = 0
            for bloom in arr:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        left, right = min(arr), max(arr)
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if canMake(mid):
                result = mid
                right = mid - 1  # Try fewer days
            else:
                left = mid + 1
        return result