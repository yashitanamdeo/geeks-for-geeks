# Problem Statement: https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

class Solution:
    def solver(self,i,arr,target,dp):
        if target == 0 : return True
        if i == 0 : return arr[i] == target
        if dp[i][target] != -1:
            return dp[i][target]
            
        notTaken = self.solver(i-1,arr,target,dp)
        taken = False
        if arr[i] <= target:
            taken = self.solver(i-1,arr,target-arr[i],dp)
            
        dp[i][target] =  taken or notTaken
        return dp[i][target]
        
        
        
    def isSubsetSum (self, arr, target):
        n = len(arr)
        dp = [[-1 for j in range(target+1)]for i in range(len(arr))]
        return self.solver(n-1,arr,target,dp)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends