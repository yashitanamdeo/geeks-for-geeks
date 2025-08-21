# Problem Statement: https://www.geeksforgeeks.org/problems/maximize-the-minimum-difference-between-k-elements/1

class Solution:
    def maxMinDiff(self, arr, k):
        low,high=0,10**5
        arr.sort()
        while low<=high:
            prev=arr[0]
            mid=(low+high)//2
            cnt=1
            for i in range(1,len(arr)):
                if arr[i]-prev>=mid:
                    cnt+=1
                    prev=arr[i]
            if cnt>=k:
                low=mid+1
            else:
                high=mid-1
        return high