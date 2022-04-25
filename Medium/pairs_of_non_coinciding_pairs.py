# Problem Statement: https://practice.geeksforgeeks.org/problems/pairs-of-non-coinciding-points4141/1

#User function Template for python3

class Solution:
    def numOfPairs(self, X, Y, n):
        # code here 
        #after solving the equation we will get x2 = x1 or y2 = y1, and discard when x1 = x2 and y1 = y2
        hmapx = {}
        hmapy = {}
        hmapxy = {}
        ans = 0
        for i in range(n):
            if X[i] in hmapx:
                ans+=hmapx[X[i]]
                hmapx[X[i]] += 1
            else:
                hmapx[X[i]] = 1
            if Y[i] in hmapy:
                ans += hmapy[Y[i]]
                hmapy[Y[i]] += 1
            else:
                hmapy[Y[i]] = 1
            if str(X[i]) + "*" +str(Y[i]) in hmapxy:
                ans -= 2*hmapxy[str(X[i]) + "*" +str(Y[i])]
                hmapxy[str(X[i]) + "*" +str(Y[i])] += 1
            else:
                hmapxy[str(X[i]) + "*" +str(Y[i])]  = 1
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        X=list(map(int,input().split()))
        Y=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.numOfPairs(X,Y,N))
# } Driver Code Ends