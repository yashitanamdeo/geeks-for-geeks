# Problem Statement: https://www.geeksforgeeks.org/problems/swapping-pairs-make-sum-equal4142/1

import bisect
class Solution:
    def findSwapValues(self, a, n, b, m):
        s1 = sum(a)
        s2 = sum(b)
        
        if abs(s2 - s1) % 2:
            return -1
        
        sum_diff = (s2 - s1) // 2
        b.sort()
        
        for val in a:
            target = sum_diff + val
            if self.binary_search(b, target):
                return 1
        
        return -1
    
    def binary_search(self, arr, target):
        index = bisect.bisect_left(arr, target)
        return index < len(arr) and arr[index] == target

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends