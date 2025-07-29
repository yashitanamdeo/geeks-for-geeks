# Problem Statement: https://www.geeksforgeeks.org/problems/max-circular-subarray-sum-1587115620/1

class Solution:
    def maxCircularSum(self, arr):
        n = len(arr)
        
        maxi = -1e9
        s = 0
        n = len(arr)
        for i in range(n):
            s += arr[i]
            maxi = max(s, maxi)
            if s < 0:
                s = 0
      
        curr_min, min_so_far = arr[0], arr[0]
        for i in arr[1:]:
            curr_min = min(curr_min + i, i)
            min_so_far = min(min_so_far, curr_min)
        ss = sum(arr)
        mx = ss - min_so_far
        if mx == 0:
            return maxi


        return max(mx, maxi)