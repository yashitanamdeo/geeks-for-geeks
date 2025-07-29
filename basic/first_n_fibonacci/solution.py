# Problem Statement: https://practice.geeksforgeeks.org/problems/print-first-n-fibonacci-numbers1002/1

# User function Template for python3

class Solution:
    # Function to return list containing first n fibonacci numbers.
    def printFibb(self, n):
        # your code here
        if n == 1:
            return [1]
        if n == 2:
            return [1, 1]

        l = [-1]*n
        l[0] = 1
        l[1] = 1
        # l[2]=1

        for i in range(2, n):
            l[i] = l[i-1]+l[i-2]

        return l


# {
 # Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):

        n = int(input())
        res = Solution().printFibb(n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
# } Driver Code Ends
