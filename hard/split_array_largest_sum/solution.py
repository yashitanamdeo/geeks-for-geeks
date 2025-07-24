# Problem Statement: https://practice.geeksforgeeks.org/problems/f04fd67b26b4828b6180715d8b1700426b637247/1

#User function Template for python3

class Solution:
    def splitArray(self, arr, n, K):
        # code here 
        def fun(mid):
            subarray = 0
            curSum = 0
            for i in arr:
                curSum+=i
                if curSum>mid:
                    subarray+=1
                    curSum=i
            return subarray+1<=K
        l,r=max(arr),sum(arr)
        res = r
        while l<=r:
            mid = l+r>>1
            if fun(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.splitArray(arr,N,K))
# } Driver Code Ends