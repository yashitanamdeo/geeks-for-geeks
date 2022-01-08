# Problem Statement: https://practice.geeksforgeeks.org/problems/n-digit-numbers-with-digits-in-increasing-order5903/1#

#User function Template for python3

class Solution:
    def increasingNumbers(self, N):
        ans = []
        if N==0:
            return ans
        else:
            if N == 1:
                ans.append(0)
            def add_digit(s, last):
                if len(s) == N:
                    ans.append(int(s))
                else:
                    for digit in range(last+1, 11-N+len(s)):
                        add_digit(s+str(digit),digit)
            add_digit("",0)
            return ans
#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.increasingNumbers(N)
        for num in ans:
            print(num,end=' ')
        print()
# } Driver Code Ends