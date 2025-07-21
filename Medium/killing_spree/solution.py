# Problem Statement: https://practice.geeksforgeeks.org/problems/killing-spree3020/1

#User function Template for python3

class Solution:
    def killinSpree (self, n):

        p = lambda n: n*(n+1)*(2*n+1)//6
        
        lo, hi = 0, n+1
        while lo < hi:
            mi = lo+(hi-lo)//2
            if p(mi) > n:
                hi = mi
            else:
                lo = mi+1
                
        return lo-1



#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ans = ob.killinSpree(N);
        print(ans)




# } Driver Code Ends