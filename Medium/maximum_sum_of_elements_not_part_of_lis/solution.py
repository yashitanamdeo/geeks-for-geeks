# Problem Statement: https://www.geeksforgeeks.org/problems/maximum-sum-of-elements-not-part-of-lis/1

import bisect

class Solution:
    def nonLisMaxSum(self, arr):
        n = len(arr)
        total_sum = sum(arr)

        # dp stores last values of increasing subsequences of different lengths
        # min_sum[i] stores the minimum sum for LIS of length i+1
        from collections import defaultdict

        dp = []
        sums = []

        for num in arr:
            pos = bisect.bisect_left(dp, num)
            if pos == len(dp):
                dp.append(num)
                if pos == 0:
                    sums.append(num)
                else:
                    sums.append(sums[pos-1] + num)
            else:
                if pos == 0:
                    if num < dp[pos]:
                        dp[pos] = num
                        sums[pos] = num
                else:
                    if sums[pos-1] + num < sums[pos]:
                        dp[pos] = num
                        sums[pos] = sums[pos-1] + num

        min_lis_sum = sums[-1]
        return total_sum - min_lis_sum
