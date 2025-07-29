# Problem Statement: https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1


from typing import List


class Solution:
    
    def countPartitions(self, n: int, d: int, arr: List[int]) -> int:
        MOD = 10**9 + 7
    
        total_sum = sum(arr)
        
        if (total_sum - d) % 2 != 0 or total_sum < d:
            return 0
        
        target = (total_sum - d) // 2
    
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % MOD
        
        return dp[target]



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
        
        n = int(input())
        
        
        d = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.countPartitions(n, d, arr)
        
        print(res)
        

# } Driver Code Ends