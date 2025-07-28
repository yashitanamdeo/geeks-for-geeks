# Problem Statement: https://practice.geeksforgeeks.org/problems/c670bf260ea9dce6c5910dedc165aa403f6e951d/1

from typing import List


class Solution:
    def getDistinctDifference(self, N: int, A: List[int]) -> List[int]:
        st = set()
        left = [0] * N
        right = [0] * N
        for i in range(N):
            left[i] = len(st)
            st.add(A[i])
        st.clear()
        for i in range(N - 1, -1, -1):
            right[i] = len(st)
            st.add(A[i])
        res = [0] * N
        for i in range(N):
            res[i] = left[i] - right[i]
        return res


#{
 # Driver Code Starts
# class IntArray:

#     def __init__(self) -> None:
#         pass

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        N = int(input())

        A = [int(i) for i in input().split()]

        obj = Solution()
        res = obj.getDistinctDifference(N, A)

        print(*res)


# } Driver Code Ends
