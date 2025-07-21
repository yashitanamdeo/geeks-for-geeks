# Problem Statement: https://practice.geeksforgeeks.org/problems/13eb74f1c80bc67d526a69b8276f6cad1b8c3401/1

#User function Template for python3

class Solution:
    def checkCompressed(self, S, T):
        # code here
        i = 0
        j = 0
        m = len(S)
        n = len(T)

        while i < m and j < n:
            if not T[j].isdigit():
                if T[j] != S[i]:
                    return 0
                i += 1
                j += 1
            else:
                k = j+1
                while k < n and T[k].isdigit():
                    k += 1
                i += int(T[j:k])
                j = k
        return 1 if i == m and j == n else 0


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        T = input()

        ob = Solution()
        print(ob.checkCompressed(S, T))
# } Driver Code Ends
