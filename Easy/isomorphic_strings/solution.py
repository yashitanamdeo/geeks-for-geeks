# Problem Statement: https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1

#User function Template for python3

class Solution:
    def areIsomorphic(self, s1, s2):
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 != len_s2:
            return False
       
        char_mapping = {}
        mapped_chars_s2 = set()
       
        for i in range(len_s1):
            char_s1, char_s2 = s1[i], s2[i]
           
            if char_s1 in char_mapping:
                if char_mapping[char_s1] != char_s2:
                    return False
            else:
                if char_s2 in mapped_chars_s2:
                    return False
               
                char_mapping[char_s1] = char_s2
                mapped_chars_s2.add(char_s2)
       
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

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
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends