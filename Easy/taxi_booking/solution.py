# Problem Statement: https://practice.geeksforgeeks.org/problems/7995e41d167d81f14f1d4194b29ef839f52d18ba/1

from typing import List


class Solution:
    def minimumTime(self, N : int, cur : int, pos : List[int], time : List[int]) -> int:
        # code here
        ans=[]
        for i in range(len(pos)):
            if cur>pos[i]:
                ans.append((cur-pos[i])*time[i])
            else:
                ans.append((pos[i]-cur)*time[i])
            
        return min(ans)
        



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
        
        N = int(input())
        
        
        cur = int(input())
        
        
        pos=IntArray().Input(N)
        
        
        time=IntArray().Input(N)
        
        obj = Solution()
        res = obj.minimumTime(N, cur, pos, time)
        
        print(res)
        

# } Driver Code Ends