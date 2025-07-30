# Problem Statement: https://www.geeksforgeeks.org/problems/subarrays-with-sum-k/1

class Solution:
    def cntSubarrays(self, arr, k):
        prefix_counts = {0: 1}
        res = 0
        curr_sum = 0

        for num in arr:
            curr_sum += num
            res += prefix_counts.get(curr_sum - k, 0)
            prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1

        return res