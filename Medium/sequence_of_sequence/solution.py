# Problem Statement: https://www.geeksforgeeks.org/problems/sequence-of-sequence1155/1

# User function Template for python3

class Solution:
    def numberSequence(self, m, n):
        # code here
        if m < n:
            return 0
        if n == 0:
            return 1
        return self.numberSequence(m/2,
                                   n-1)+self.numberSequence(m-1, n)


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        m = int(arr[0])
        n = int(arr[1])

        ob = Solution()
        print(ob.numberSequence(m, n))
# } Driver Code Ends
