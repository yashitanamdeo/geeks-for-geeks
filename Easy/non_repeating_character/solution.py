# Problem Statement: https://practice.geeksforgeeks.org/problems/non-repeating-character-1587115620/1

# User function Template for python3

import sys
import io
import atexit
from collections import Counter


class Solution:
    # Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self, s):
        # code here9
        ss = Counter(s)
        for i in s:
            if ss[i] == 1:
                return i
        return '$'


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
        obj = Solution()
        ans = obj.nonrepeatingCharacter(s)
        if (ans != '$'):
            print(ans)
        else:
            print(-1)

# } Driver Code Ends
