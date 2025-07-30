# Problem Statement: https://practice.geeksforgeeks.org/problems/466faca80c3e86f13880710491c634d26abd44a7/1

#User function Template for python3

class Solution:
    
    #Function to remove pair of duplicates from given string using Stack.
    def removePair(self,s):
        st = []
        for i in range(len(s)):
            if st and st[-1] == s[i]:
                st.pop()
            else:
                st.append(s[i])
        if not st:
            return -1
        return "".join(st)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        obj = Solution()
        print(obj.removePair(str(input())))
# } Driver Code Ends