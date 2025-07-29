# Problem Statement: https://practice.geeksforgeeks.org/problems/count-the-subarrays-having-product-less-than-k1708/1

#User function Template for python3

from itertools import combinations
class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        count = 0
        product = 1
        left = 0

        for right in range(n):
            product *= a[right]

            while product >= k and left <= right:
                product /= a[left]
                left += 1

            count += right - left + 1

        return count
    
    
    
    


#{ 
 # Driver Code Starts

#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
