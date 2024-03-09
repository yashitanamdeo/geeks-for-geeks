# Problem Statement: https://www.geeksforgeeks.org/problems/find-the-n-th-character5925/1

#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        if n==0:
            return s[0]
        for i in range(r):
            temp=""
            for j in range(n//2 +1):
                if s[j]=="0":
                    temp+="01"
                else:
                    temp+="10"
            s=temp[:]
        return s[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends