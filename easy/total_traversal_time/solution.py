# Problem Statement: https://practice.geeksforgeeks.org/problems/5ae4f296db3e6bb74641c4087d587b6f89d9d135/1

from collections import defaultdict
from typing import List


class Solution:
    def totalTime(self, n: int, arr: List[int], time: List[int]) -> int:
        # code here
        ans = 0
        dic = defaultdict(int)
        for i in range(0, n):
            if arr[i] not in dic:
                ans += 1
                dic[arr[i]] += 1
            else:
                ans += time[arr[i]-1]
                dic[arr[i]] += 1
        return ans-1


# {
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        time = IntArray().Input(n)

        obj = Solution()
        res = obj.totalTime(n, arr, time)

        print(res)


# } Driver Code Ends
