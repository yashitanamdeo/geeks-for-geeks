# Problem Statement: https://practice.geeksforgeeks.org/problems/fda70097eb2895ecfff269849b6a8aace441947c/1

#User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        # code here
        a = set(A)
        b = set(B)
        if b.issubset(a):
            S = ""
            ans = 0
            while len(S) < len(B):
                S += A
                ans += 1
            if B in S:
                return ans
            elif B in S+A:
                return ans + 1
            else:
                return -1
        else:
            return -1


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = input()
        B = input()

        ob = Solution()
        print(ob.minRepeats(A, B))
# } Driver Code Ends
