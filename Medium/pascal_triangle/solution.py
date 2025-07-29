# Problem Statement: https://www.geeksforgeeks.org/problems/pascal-triangle0652/1

# User function Template for python3

# User function Template for python3
class Solution:
    def nthRowOfPascalTriangle(self, n):
        MOD = 10**9 + 7
        row = [1]
        for i in range(1, n):
            row.append((row[i-1] * (n-i)) % MOD * pow(i, MOD-2, MOD) % MOD)
        return row


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.nthRowOfPascalTriangle(n)
        for x in ans:
            print(x, end=" ")
        print()
        tc = tc-1
# } Driver Code Ends
