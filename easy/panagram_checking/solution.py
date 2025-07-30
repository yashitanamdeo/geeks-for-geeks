# Problem Statement: https://www.geeksforgeeks.org/problems/pangram-checking-1587115620/1

#User function Template for python3

class Solution:
    def checkPangram(self,s):
        return len(set([i.lower() for i in s if ord(i)>=97 and ord(i)<=122 or ord(i)>=65 and ord(i)<=90]))==26 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        obj = Solution()
        if(obj.checkPangram(s)):
            print(1)
        else:
            print(0)
# } Driver Code Ends