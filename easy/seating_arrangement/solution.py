# Problem Statement: https://practice.geeksforgeeks.org/problems/6bb49b563cc171335c6564b00307a6d867e0268d/1


from typing import List


class Solution:
    def is_possible_to_get_seats(self, n: int, m: int, seats: List[int]) -> bool:
        for i in range(m):
            if seats[i] == 0:
                front_empty = False
                next_empty = False
                if i-1 < 0 or seats[i-1] == 0:
                    front_empty = True
                if i+1 >= m or seats[i+1] == 0:
                    next_empty = True
                if front_empty and next_empty:
                    n -= 1
                    seats[i] = 1
        if n <= 0:
            return True
        return False


#{
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

        m = int(input())

        seats = IntArray().Input(m)

        obj = Solution()
        res = obj.is_possible_to_get_seats(n, m, seats)

        result_val = "Yes" if res else "No"
        print(result_val)

# } Driver Code Ends
