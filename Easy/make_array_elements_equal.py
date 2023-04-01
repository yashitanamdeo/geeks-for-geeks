# Problem Statement: https://practice.geeksforgeeks.org/problems/1f05c7c12b1084f270c57566b2110967c046730d/1

#User function Template for python3

class Solution:
    def minOperations(self, N):
        return (N*N)//4


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        N = int(input())
        ob = Solution()
        print(ob.minOperations(N))

        T -= 1

# } Driver Code Ends
