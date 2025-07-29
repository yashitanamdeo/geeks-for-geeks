# Problem Statement: https://www.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places-1587115620/1

# User function Template for python3


import sys
import io
import atexit


class Solution:
    # Function to check if a string can be obtained by rotating
    # another string by exactly 2 places.
    def isRotated(self, str1, str2):
        n = len(str1)
        if n != len(str2):
            return False
        cw, acw = True, True
        for i in range(n):
            if str1[i] != str2[(i+2) % n]:
                cw = False
            if str1[i] != str2[(i-2) % n]:
                acw = False
            if not cw and not acw:
                break
        return cw or acw


# {
 # Driver Code Starts
# Initial Template for Python 3


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        p = str(input())
        if (Solution().isRotated(s, p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends
