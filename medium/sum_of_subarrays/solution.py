# Problem Statement: https://www.geeksforgeeks.org/problems/sum-of-subarrays2229/1

class Solution:
    def subarraySum(self, arr):
        total = 0
        prev = 0
        for i in arr:
            total += prev + i
            prev += i
            
        n = len(arr)
        total *= n
        i = 0
        while n and i < len(arr):
            total -= (arr[i] * n * (n - 1))
            n -= 1
            i += 1
            
        return total