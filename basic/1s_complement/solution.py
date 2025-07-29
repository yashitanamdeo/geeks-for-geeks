# Problem Statement: https://practice.geeksforgeeks.org/problems/1s-complement2819/1#

#User function Template for python3
class Solution:
    def onesComplement(self,S,N):
        # code here
        complement = ''
        for i in range(N):
            if S[i] == '0':
                complement += '1'
            else:
                complement += '0'
        return complement

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        S = input()

        ob = Solution()
        print(ob.onesComplement(S,N))
# } Driver Code Ends