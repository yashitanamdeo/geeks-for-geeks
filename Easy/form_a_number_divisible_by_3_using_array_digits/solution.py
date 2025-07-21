# Problem Statement: https://practice.geeksforgeeks.org/problems/form-a-number-divisible-by-3-using-array-digits0717/1

#User function Template for python3

class Solution:
    def isPossible(self, N, arr):
        # code here
        return 1 if sum(arr)%3==0 else 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.isPossible(N, arr))
# } Driver Code Ends