# Problem Statement: https://practice.geeksforgeeks.org/problems/maximum-sum-of-increasing-order-elements-from-n-arrays4848/1#

#User function Template for python3

def maximumSum(n, m, arr):    
    for sub_arr in arr:
        sub_arr.sort()
    sum = 0
    last = None
    for i in range(n-1,-1,-1):
        if last:
            sub_arr = arr[i]
            not_find = True
            for j in range(len(sub_arr)-1,-1,-1):
                curr = arr[i][j]
                if curr < last:
                    sum += curr
                    last = curr
                    not_find = False
                    break
            if not_find:
                return 0
        else:
            last = max(arr[i])
            sum = last
    
    return sum


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n, m = map(int , input().split())
    arr = []
    for i in range(0, n):
        ll = list(map(int, input().strip().split()))
        arr.append(ll)
    ans = maximumSum(n, m, arr)
    print(ans)




# } Driver Code Ends