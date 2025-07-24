# Problem Statement: https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1

#User function Template for python3

class Solution:
    def armstrongNumber(self, n: int) -> str:
        # Step 1: Extract the digits
        hundreds = n // 100
        tens = (n // 10) % 10
        units = n % 10

        # Step 2: Compute the sum of cubes of digits
        sum_of_cubes = (hundreds ** 3) + (tens ** 3) + (units ** 3)

        # Step 3: Compare the sum with the original number
        if sum_of_cubes == n:
            return "true"
        else:
            return "false"

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends