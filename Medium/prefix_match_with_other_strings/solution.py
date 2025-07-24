# Problem Statement: https://practice.geeksforgeeks.org/problems/prefix-match-with-other-strings/1

# User function Template for python3

class Solution:
    def klengthpref(self, arr, n, k, s):
        # return list of words(str) found in the
        c = 0
        if len(s) < k:
            return 0
        p = s[:k]

        for x in arr:
            if x[:k] == p:
                c += 1
        return c


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = []
        for x in range(n):
            s1 = input()
            arr.append(s1)
        k = int(input())
        s = input()
        obj = Solution()
        print(obj.klengthpref(arr, n, k, s))


# } Driver Code Ends
