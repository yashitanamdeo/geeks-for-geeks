# Problem Statement: https://practice.geeksforgeeks.org/problems/maximum-average-subarray5859/1#

#User function Template for python3

class Solution:
    def findMaxAverage(self, arr, n, k):
        # code here
        if n < k:
            return 0
        Sum = sum(arr)
        
        temp = Sum
        answer = 0
        
        for i in range(k,n):
            Sum += arr[i] - arr[i-k]
            if Sum >= temp:
                temp = Sum
                answer = i - k + 1
                
        return answer
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxAverage(arr, n, k)
        for i in range(ans, ans+k):
            print(arr[i], end=" ")
        print()
        tc -= 1
# } Driver Code Ends