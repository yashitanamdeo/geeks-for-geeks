# Problem Statement: https://practice.geeksforgeeks.org/problems/find-patterns0606/1

#User function Template for python3
class Solution:
    def numberOfSubsequences(self, S, W):

        # code here
        S = list(S)
        counter = 0

        for i in range(len(S)):
            k = 0

            for j in range(i, len(S)):
                if S[j] == W[k]:
                    k += 1
                    S[j] = "*"
                if k == len(W):
                    counter += 1
                    break
        return counter


#{
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        S = str(input())
        W = str(input())

        ob = Solution()
        print(ob.numberOfSubsequences(S, W))

# } Driver Code Ends
