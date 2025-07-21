# Problem Statement: https://practice.geeksforgeeks.org/problems/capacity-to-ship-packages-within-d-days/1

#User function Template for python3

class Solution:
    def leastWeightCapacity(self, arr, N, D):
        # code here 
        def isPossible(arr,D,mid):
            no_of_days = 1
            shipped_goods = 0
            for i in range(len(arr)):
                if (arr[i] + shipped_goods) <= mid:
                    shipped_goods += arr[i]
                else:
                    no_of_days +=1
                    if no_of_days>D or arr[i]>mid:
                        return False
                    shipped_goods = arr[i]
            return True
    
        start = 0
        end = sum(arr)
        ans = -1
        mid = start + (end-start)//2
            
        while start<=end:
            if isPossible(arr,D,mid):
                ans = mid
                end = mid-1
            else:
                start = mid+1
                
            mid = start + (end-start)//2
                
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        D=int(input())
        
        ob = Solution()
        print(ob.leastWeightCapacity(arr,N,D))
# } Driver Code Ends