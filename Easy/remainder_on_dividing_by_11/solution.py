# Problem Statement: https://practice.geeksforgeeks.org/problems/aa8c89caad6b5c3a76ba5e6d65454f77aac3f3543526/1

#User function Template for python3


class Solution:
    def xmod11(self, x):
        #code here
        return int(x) % 11


#{
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tcs = int(input())
    for _ in range(tcs):
        x = input()

        ob = Solution()

        print(ob.xmod11(x))

# } Driver Code Ends
