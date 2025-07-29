# Problem Statement: https://practice.geeksforgeeks.org/problems/badefd58bace4f2ca25267ccfe0c9dc844415e90/1

# User function Template for python3

from typing import List


class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:

        # returns true if the signs of given                                                         integers are different, otherwise false
        def oppositeSigns(x, y): return ((x ^ y) < 0)

        if len(arr) > 0:
            i = 1
            # for i in range(1,len(arr)):
            while i < len(arr):

                if oppositeSigns(arr[i], arr[i-1]):

                    arr.pop(i-1)
                # when i-1th gets deleted, ith element becomes i-1

                    arr.pop(i-1)

# as two elements gets deleted arr.length decremented by 2, hence we need to decrease i by 1 unless i=1
                    if i != 1:
                        i = i-1

                else:
                    i = i+1

                # if array empty then return
                # if len(arr) == 0 :break

        return arr


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = list(map(int, input().split()))

        obj = Solution()
        res = obj.makeBeautiful(arr)
        print(*res)
# } Driver Code Ends
