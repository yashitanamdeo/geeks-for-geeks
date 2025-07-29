# Problem Statement: https://practice.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream1216/1

# User function Template for python3

from collections import OrderedDict


class Solution:
    def FirstNonRepeating(self, A):
        # Code here
        out = ""
        dic = OrderedDict()
        for i in A:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            s = 0
            for i, j in dic.items():
                if j == 1:
                    out += i
                    s = 1
                    break
            if s == 0:
                out += '#'
        return out


# {
 # Driver Code Starts

# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        A = input()
        ob = Solution()
        ans = ob.FirstNonRepeating(A)
        print(ans)

# } Driver Code Ends
