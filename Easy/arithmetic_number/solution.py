# Problem Statement: https://practice.geeksforgeeks.org/problems/arithmetic-number2815/1

#User function Template for python3

class Solution:
    def inSequence(self, A, B, C):
        # code here
        if C == 0:
            return 1 if A == B else 0
        n = (B-A)//C + 1
        return 1 if B == A+(n-1)*C and n > 0 else 0


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B, C = [int(x) for x in input().split()]

        ob = Solution()
        print(ob.inSequence(A, B, C))
# } Driver Code Ends
