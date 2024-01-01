# Problem Statement: https://www.geeksforgeeks.org/problems/array-pair-sum-divisibility-problem3257/1

from collections import defaultdict


class Solution:
    def canPair(self, nums, k):
        # Code here
        if len(nums) % 2 != 0:
            return False
        count = defaultdict(int)
        for ele in nums:
            count[ele % k] += 1
        for key in count.keys():
            if count[key] % 2 != 0 and count[key] != count[k - key]:
                return False
        return True


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, k = input().split()
        n = int(n)
        k = int(k)
        nums = list(map(int, input().split()))
        ob = Solution()
        ans = ob.canPair(nums, k)
        if (ans):
            print("True")
        else:
            print("False")
# } Driver Code Ends
