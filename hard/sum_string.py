# Problem Statement: https://www.geeksforgeeks.org/problems/sum-string3151/1

#User function Template for python3
class Solution:
    def isSumString (ob, s):
        # code here 
        n = len(s)
        def check(i, j, k):
            nonlocal s, n
            if k == n:
                return True
            if k > n:
                return False
            n1 = int(s[i:j])
            n2 = int(s[j:k])
            ns = str(n1+n2)
            if not s[k:].startswith(ns):
                return False
            return check(j, k, k+len(ns))
        
        for i in range(1, n):
            for j in range(i+1, n):
                if check(0, i, j):
                    return 1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        
        print(ob.isSumString(S))
# } Driver Code Ends