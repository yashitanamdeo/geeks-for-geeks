# Problem Statement: https://www.geeksforgeeks.org/problems/swap-two-nibbles-in-a-byte0446/1

#User function Template for python3
class Solution:
    def swapNibbles (self, n):
        x = bin(n)
        x = x[2:]
        x = "0"*(8-len(x)) + x
        x = x[4:]+x[:4]
        return int(x,2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.swapNibbles(n))

# } Driver Code Ends