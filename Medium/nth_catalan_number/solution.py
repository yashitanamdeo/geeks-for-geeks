# Problem Statement: https://practice.geeksforgeeks.org/problems/nth-catalan-number0817/1


class Solution:
    def findCatalan(self, n: int) -> int:
        if n <= 1:
            return 1

        MOD = 10**9 + 7
        catalan = [0] * (n + 1)
        catalan[0] = catalan[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                catalan[i] = (catalan[i] + (catalan[j] * catalan[i - j - 1])) % MOD

        return catalan[n]
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.findCatalan(n)
        
        print(res)
        

# } Driver Code Ends