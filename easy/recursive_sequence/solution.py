# Problem Statement: https://www.geeksforgeeks.org/problems/recursive-sequence1611/1

#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        MOD=10**9+7
        sum_val=0
        add=1
        for i in range(n):
            prd=1
            for j in range(i+1):
                prd=(prd*add) % MOD
                add += 1
            sum_val=(sum_val+prd)%MOD
        return sum_val


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends