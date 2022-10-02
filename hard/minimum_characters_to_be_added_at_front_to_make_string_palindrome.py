# Problem Statement: https://practice.geeksforgeeks.org/problems/minimum-characters-to-be-added-at-front-to-make-string-palindrome/1

class Solution:

    def minChar(self, s):
        ha = [0]*len(s)
        i, j = 0, len(s)-1
        ans = 0
        while i < j:
            if s[i] == s[j]:
                if i == 0:
                    ha[i] = 1
                else:
                    ha[i] = 1+ha[i-1]
                i += 1
                j -= 1
            else:
                if i == 0:
                    ans = len(s)-j
                    j -= 1
                else:
                    i = ha[i-1]//2
                    ans = (len(s)-(j+1))-i
        return ans


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
# } Driver Code Ends
