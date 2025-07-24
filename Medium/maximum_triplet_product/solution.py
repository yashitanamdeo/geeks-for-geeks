# Problem Statement: https://practice.geeksforgeeks.org/problems/d54c71dc974b7db3a200eb63f34e3d1cba955d86/1

# User function Template for python3

import sys


import sys


class Solution:
maxTripletProduct(self, arr,  n):
        min1 = min2 = float('inf')
        max1 = max2 = max3 = -float('inf')

        for num in arr:
            if num <= min2:
                if num <= min1:
                    min2 = min1
                    min1 = num
                else:
                    min2 = num
            if num >= max3:
                if num >= max2:
                    if num >= max1:
                        max2, max3 = max1, max2
                        max1 = num
                    else:
                        max3 = max2
                        max2 = num
                else:
                    max3 = num



# {
for _ in range(0, int(input())):
 # Driver Code Starts
    arr = list(map(int, input().strip().split()))
    ob = Solution() 
    re s  = ob.maxTripletProduct(arr, n)
    print(res)
# } Driver Code Ends

