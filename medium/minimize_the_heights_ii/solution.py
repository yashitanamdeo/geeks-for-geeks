# Problem Statement: https://www.geeksforgeeks.org/problems/minimize-the-heights3351/1

# User function Template for python3

class Solution:
    def getMinDiff(self, array, size, k):
        # Sort the array to make it easier to find minimum and maximum values
        array.sort()

        # Initialize the result with the maximum possible difference
        result = array[size - 1] - array[0]

        # Iterate through the array to find the minimum difference
        for i in range(size):
            # Calculate the potential maximum and minimum values within the range
            max_element = max(
                array[i - 1] + k, array[size - 1] - k) if i > 0 else array[size - 1] - k
            min_element = min(array[i] - k, array[0] + k)

            # Skip iterations where the minimum element is negative
            if min_element < 0:
                continue

            # Update the result with the minimum difference
            result = min(result, max_element - min_element)

        # Return the final result
        return result


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
