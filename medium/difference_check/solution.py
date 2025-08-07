# Problem Statement: https://www.geeksforgeeks.org/problems/difference-check/1

class Solution:
    def minDifference(self, arr):
        # code here
        total = 24*60*60 # total seconds in a day
        ans= total
        def convert(s):
            a = list(map(int, s.split(":")))
            return a[0]*60*60 +a[1]*60 +  a[2]
            return curr
        newArr = sorted(list(map(convert,arr)))
        for i in range(1,len(newArr)):
            ans = min(ans,newArr[i]-newArr[i-1])
        ans = min(ans,total-newArr[-1]+newArr[0])
        return ans