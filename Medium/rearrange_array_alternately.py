# Problem Statment: https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately-1587115620/1

#User function Template for python3
import math


class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
   def rearrange(self, arr, n):
       ans, pos = [], 0

       while pos <= n-1-pos:
            ans += [arr[n-1-pos], arr[pos]]
            pos += 1

        for i in range(n):
            arr[i] = ans[i]


#{
 # Driver Code Starts
#Initial Template for Python 3


def main():
      T = int(input())
       while(T > 0):

            n = int(input())

            arr = [int(x) for x in input().strip().split()]

            ob = Solution()
            ob.rearrange(arr, n)

            for i in arr:
                print(i, end=" ")

            print()

            T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
