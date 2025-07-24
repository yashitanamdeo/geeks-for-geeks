# Problem Statement: https://practice.geeksforgeeks.org/problems/839d6ba2c2e4c669ba9d9d9f32ad20118937284e/1

#{
# Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def countSubstring(self, s):
        #code here
        n = len(s)
        count = 0
        for i in range(n):
            a = 0
            for j in range(i, n):
                if s[j].isupper():
                    a += 1
                else:
                    a += -1
                if a == 0:
                    count += 1
        return count


#{
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countSubstring(S)
        print(ans)

# } Driver Code Ends
