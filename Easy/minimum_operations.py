# Problem Statement: https://practice.geeksforgeeks.org/problems/find-optimum-operation4504/1

# User function Template for python3

class Solution:
    def minOperation(self, n):
        # Initialize a variable to keep track of the number of operations.
        operation_count = 0

        # Continue the loop until n becomes zero.
        while n > 0:
            # If n is odd, subtract 1; otherwise, divide it by 2.
            if n % 2:
                n -= 1
            else:
                n //= 2

            # Increment the operation count for each step.
            operation_count += 1

        # Return the total number of operations required to reach zero.
        return operation_count


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.minOperation(n))
# } Driver Code Ends
