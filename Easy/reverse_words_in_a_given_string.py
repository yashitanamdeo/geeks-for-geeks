# Problem Statement: https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1#


# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        ans = ''
        S = S.split(".")
        ans = S[::-1]
        return ".".join(ans)
            
#{ 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends