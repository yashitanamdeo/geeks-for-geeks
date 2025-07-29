# Problem Statement: https://practice.geeksforgeeks.org/problems/d894706c496da5c5a4f45b0360c7f4164c516f83/1

from typing import List
from collections import Counter


class Solution:
    def powerfullInteger(self, n: int, intervals: List[List[int]], k: int) -> int:
        counts = Counter()
        for start, end in intervals:
            counts[start] += 1
            counts[end + 1] -= 1
        current_count = 0
        powerfull_integer = -1
        for i in sorted(counts):
            # The last index will be +1 after the last interval
            # and will have negative change, hence we first
            # check if the current count is greater than "k"
            # which means that the previous integer "i - 1"
            # was the maximum one.
            if current_count >= k:
                powerfull_integer = i - 1
            current_count += counts[i]
        return powerfull_integer


#{
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        intervals = IntMatrix().Input(n, 2)

        k = int(input())

        obj = Solution()
        res = obj.powerfullInteger(n, intervals, k)

        print(res)


# } Driver Code Ends
