# Problem Statement: https://www.geeksforgeeks.org/problems/maximize-number-of-1s0905/1

class Solution:
    def maxOnes(self, arr, k):
        zero=0
        left=0
        ans=0
        for right in range(len(arr)):
            if arr[right]==0:
                zero+=1
            while zero>k:
                if arr[left]==0:
                    zero-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans