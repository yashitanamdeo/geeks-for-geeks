# Problem Statement: https://practice.geeksforgeeks.org/problems/two-numbers-with-odd-occurrences5846/1

# User function Template for python3
class Solution:

    def twoOddNum(self, Arr, N):

        occur = {}
        for i in Arr:
            occur[i] = occur.get(i, 0)+1
        res = []
        for keys in occur:
            if occur[keys] % 2 != 0:
                res.append(keys)
        res.sort()
        return res[::-1]


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution()
        ans = ob.twoOddNum(Arr, N)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
# } Driver Code Ends
