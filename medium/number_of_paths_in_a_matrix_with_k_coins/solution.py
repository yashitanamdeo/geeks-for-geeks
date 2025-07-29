# Problem Statement: https://www.geeksforgeeks.org/problems/number-of-paths-in-a-matrix-with-k-coins2728/1

#User function Template for python3

class Solution:
    def numberOfPath (self, n, k, arr):
        # top-left to bottom-right taking down and right move
        dp = {} # key (r,c,k): no_of_ways
        def dfs(r,c,k):
            # either out of bound or unreachable with k coin => no way
            if max(r,c) >= n or arr[r][c] > k:
                return 0
            # if already computed return it
            if (r,c,k) in dp:
                return dp[(r,c,k)]
            # reached destination with k coin return 1 else 0
            if r == c == n - 1:
               return 1 if arr[r][c] == k else 0
            
            right = dfs(r,c+1,k - arr[r][c])
            down = dfs(r+1,c,k - arr[r][c])
            res = dp[(r,c,k)] = right + down
            return res
        return dfs(0,0,k)




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        k= int(input())
        n=int(input())
        l = list(map(int, input().split()))
        arr = list()
        c=0
        for i in range(0, n):
            temp = list()
            for j in range(0, n):
                temp.append(l[c])
                c += 1
            arr.append(temp)
        ans = ob.numberOfPath(n, k, arr);
        print(ans)


# } Driver Code Ends