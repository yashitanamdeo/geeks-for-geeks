# Problem Statement: https://www.geeksforgeeks.org/problems/nuts-and-bolts-problem0431/1

#User function Template for python3
class Solution:

    def matchPairs(self, n, nuts, bolts):
        bolts.sort()
        nuts.sort()
        return nuts,bolts

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(n, nuts, bolts)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends