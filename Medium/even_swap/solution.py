# Problem Statement: https://practice.geeksforgeeks.org/problems/even-swap/1

#User function Template for python3

from typing import List


class Solution():
    def lexicographicallyLargest(self, a, n):
        #your code here
        i = 0
        while i < n:
            j = i + 1
            while j < n and (a[j] % 2 + a[j - 1]) % 2 == 0:
                j += 1
            a[i:j] = sorted(a[i:j], reverse=True)
            i = j
        return a


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        ans = Solution().lexicographicallyLargest(a, n)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends
