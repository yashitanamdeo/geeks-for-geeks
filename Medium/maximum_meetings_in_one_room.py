# Problem Statement: https://www.geeksforgeeks.org/problems/maximum-meetings-in-one-room/1/

from typing import List


class Solution:
    def maxMeetings(self, n: int, s: List[int], f: List[int]) -> List[int]:
        # code here
        pairs = []
        for i in range(N):
            pairs.append([S[i], F[i], i+1])
        pairs.sort(key=lambda x: x[1])
        count = []
        curr = pairs[0][1]
        count.append(pairs[0][2])
        for i in range(1, N):
            if pairs[i][0] > curr:
                count.append(pairs[i][2])
                curr = pairs[i][1]
        count.sort()
        return count


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

        N = int(input())

        S = IntArray().Input(N)

        F = IntArray().Input(N)

        obj = Solution()
        res = obj.maxMeetings(N, S, F)

        IntArray().Print(res)


# } Driver Code Ends
