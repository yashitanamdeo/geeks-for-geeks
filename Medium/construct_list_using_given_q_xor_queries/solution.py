# Problem Statement: https://www.geeksforgeeks.org/problems/construct-list-using-given-q-xor-queries/1


from typing import List

class Solution:
    def constructList(self, q, queries):
        ans = []
        run_xor = 0
        for q in reversed(queries):
            if q[0] == 0:
                q[1] ^= run_xor
                ans.append(q[1])
            else:
                run_xor ^= q[1]
        ans.append(run_xor)
        return sorted(ans)



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


class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        q = int(input())

        queries = IntMatrix().Input(q, 2)

        obj = Solution()
        res = obj.constructList(q, queries)

        IntArray().Print(res)

# } Driver Code Ends