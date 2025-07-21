# Problem Statement: https://practice.geeksforgeeks.org/problems/distinct-palindromic-substrings5141/1

#User function Template for python3

class Solution:
    def palindromeSubStrs(self, s):
       # code here
       res=set()
       for i in range(len(s)):
           l=i
           h=i
           while l>=0 and h<len(s) and s[l]==s[h]:
               res.add(s[l:h+1])
               l-=1
               h+=1
           l=i
           h=i+1
           while l>=0 and h<len(s) and s[l]==s[h]:
               res.add(s[l:h+1])
               l-=1
               h+=1
           
       return len(res)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.palindromeSubStrs(Str))
# } Driver Code Ends