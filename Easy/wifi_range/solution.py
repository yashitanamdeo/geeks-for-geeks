# Problem Statement: https://practice.geeksforgeeks.org/problems/61567fb59e9f202db5cc2ad320ffeb6d95bf72d7/1

#User function Template for python3
class Solution:
    def wifiRange(self, n, s, x):
        l = 0
        for i in range(n):
            if(s[i] == '0'):
                l += 1
            if(s[i] == '1'):
                l = -x
            if(l > x):
                return False

        if(l > 0):
            return False
        return True


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, X = map(int, input().strip().split())
        S = input()
        ob = Solution()
        ans = ob.wifiRange(N, S, X)
        if ans:
            print(1)
        else:
            print(0)

# } Driver Code Ends
