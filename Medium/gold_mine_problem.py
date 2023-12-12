# Problem Statement: https://www.geeksforgeeks.org/problems/gold-mine-problem2608/1

# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        for j in range(m-1,0,-1):
            for i in range(1,n+1):
                temp=0
                for dx in [-1,0,1]:
                    x=i+dx
                    if x>0 and x<=n:
                        temp=max(temp,M[x-1][j])
                M[i-1][j-1]+=temp
        res=0
        for i in range(1,n+1):
            res=max(res,M[i-1][0])
        return res


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends