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
        #return '.'.join(S.split('.')[::-1])

    '''
    def reverseWords(self,S):
        list1=S.split('.')
        ans_str=''
        for i in range(len(list1)-1,-1,-1):
            if i >0:
                ans_str=ans_str+list1[i]+'.'
            elif i==0:
                ans_str=ans_str+list1[i]
        return ans_str
    '''
            
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