# Problem Statement: https://practice.geeksforgeeks.org/problems/count-number-of-substrings4528/1

# User function Template for python3

class Solution:
    def atmost(self, s, k):
        n = len(s)
        left, right = 0, 0
        result = 0
        distinct = 0
        freq = [0]*26
        while right < n:
            freq[ord(s[right])-ord("a")] += 1
            if freq[ord(s[right])-ord("a")] == 1:
                distinct += 1
            while distinct > k:
                freq[ord(s[left])-ord("a")] -= 1
                if freq[ord(s[left])-ord("a")] == 0:
                    distinct -= 1
                left += 1
            result += right-left+1
            right += 1
        return result

    def substrCount(self, s, k):
        return self.atmost(s, k)-self.atmost(s, k-1)


# {
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())
for tc in range(t):
    s = input()
    k = int(input())
    ob = Solution()
    print(ob.substrCount(s, k))
# } Driver Code Ends
