# Problem Statement: https://practice.geeksforgeeks.org/problems/55dbfdc246f3f62d6a7bcee7664cacf6be345527/1

#User function Template for python3

class Solution:
    def addMinChar(self, str1):
        s = str1 + "@" + str1[::-1]
        n = len(s)
        p = [0]*(n+1)
        p[0] = -1
        for i in range(1, n+1):
            k = p[i-1]
            while k > 0 and s[k] != s[i-1]:
                k = p[k]
            p[i] = k+1
        return len(str1) - p[n]


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str1 = input()

        ob = Solution()
        print(ob.addMinChar(str1))

# } Driver Code Ends
