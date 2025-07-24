# Problem Statement: https://practice.geeksforgeeks.org/problems/the-smurfs4201/1

#User function Template for python3


class Solution:

    def minFind(self, n, a):

        # code here
        r = a.count('R')
        g = a.count('G')
        b = a.count('B')

        if(max(r, max(b, g)) == n):
            return n
        elif r % 2 == b % 2 and r % 2 == g % 2:
            return 2
        return 1


#{
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()

        ob = Solution()
        print(ob.minFind(n, a))
# } Driver Code Ends
