# Problem Statement: https://practice.geeksforgeeks.org/problems/find-k-th-smallest-element-in-given-n-ranges/1


from typing import List


class Solution:
    def kthSmallestNum(self, n: int, ranges: List[List[int]], q: int, queries: List[int]) -> List[int]:
        # Sort ranges based on the start value
        ranges.sort()

        # Find missing elements to determine skip and
        # count the number of unique elements in each interval
        skip = [0] * n
        count = [0] * n

        if ranges[0][0] > 1:
            skip[0] = ranges[0][0] - 1

        count[0] = ranges[0][1] - ranges[0][0] + 1

        for i in range(1, n):
            gap = ranges[i][0] - ranges[i - 1][1] - 1
            skip[i] = skip[i - 1] + max(0, gap)

            count[i] = count[i - 1]

            # Check for overlap
            if ranges[i - 1][1] >= ranges[i][0]:
                count[i] += ranges[i][1] - ranges[i - 1][1] + 1
            else:
                count[i] += ranges[i][1] - ranges[i][0] + 1

        # Serve each query and determine the interval in which the kth element lies
        ans = [-1] * q

        for i in range(q):
            idx = -1

            # Find the interval where the ith element belongs, if it exists
            for j in range(n):
                if queries[i] <= count[j]:
                    idx = j
                    break

            # If the interval exists, find the target value
            if idx != -1:
                ans[i] = skip[idx] + queries[i]

        return ans


# {
 # Driver Code Starts


class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


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

        ranges = IntMatrix().Input(n, 2)

        q = int(input())

        queries = IntArray().Input(q)

        obj = Solution()
        res = obj.kthSmallestNum(n, ranges, q, queries)

        IntArray().Print(res)


# } Driver Code Ends
