# Problem Statement: https://www.geeksforgeeks.org/problems/maximize-median-after-doing-k-addition-operation/1

class Solution:
    def maximizeMedian(self, arr, k):
        arr.sort()
        n = len(arr)
        idx = (n - 1) // 2

        def canMake(mid):
            diff = 0
            for i in range(idx, n):
                if mid >= arr[i]:
                    diff += mid - arr[i]
                if diff > k:
                    return False
            return True
            
        l = arr[idx]
        r = arr[-1] + k

        while l <= r:
            mid = (l + r) // 2
            if canMake(mid):
                l = mid + 1
            else:
                r = mid - 1
            
        if n % 2 == 1:
            return r
            
        return (r + max(r, arr[idx + 1])) // 2
