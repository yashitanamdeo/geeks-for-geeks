# Problem Statement: https://www.geeksforgeeks.org/problems/wildcard-string-matching1126/1

#User function Template for python3

import re

class Solution:
    def match(self, wildcard, text_to_match):
        # Convert the wildcard pattern to a regular expression pattern
        regex_pattern = '^' + wildcard.replace('?', '.').replace('*', '.*') + '$'

        # Use re.fullmatch to check if the entire text matches the regular expression pattern
        return True if re.fullmatch(regex_pattern, text_to_match) else False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        wild = input()
        pattern = input()
        
        ob = Solution()
        if(ob.match(wild, pattern)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends