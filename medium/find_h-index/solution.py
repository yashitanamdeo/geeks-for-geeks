# Problem Statement: https://www.geeksforgeeks.org/problems/find-h-index--165609/1

class Solution:
    def hIndex(self, ct):
        ct.sort()
        ans,n=0,len(ct)
        for i in range(n):
            ans=max(ans,min(ct[i],n-i))
        return ans