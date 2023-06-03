# Problem Statement: https://practice.geeksforgeeks.org/problems/find-maximum-equal-sum-of-three-stacks/1

from typing import List


class Solution:
    def maxEqualSum(self, N1:int, N2:int, N3:int, S1 : List[int], S2 : List[int], S3 : List[int]) -> int:
        suffix_sums = []
        for s, n in ((S1, N1), (S2, N2), (S3, N3)):
            n = len(s)
            suffix_sum = [0] * (n + 1)
            for i in range(n - 1, -1, -1):
                suffix_sum[i] = s[i] + suffix_sum[i + 1]
            suffix_sums.append(suffix_sum)
        return max(set.intersection(*map(set, suffix_sums)))
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(3)
        
        
        S1=IntArray().Input(a[0])
        
        
        S2=IntArray().Input(a[1])
        
        
        S3=IntArray().Input(a[2])
        
        obj = Solution()
        res = obj.maxEqualSum(a[0],a[1],a[2], S1, S2, S3)
        
        print(res)
        

# } Driver Code Ends