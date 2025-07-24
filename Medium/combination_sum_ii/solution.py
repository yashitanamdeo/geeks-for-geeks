# Problem Statement: https://www.geeksforgeeks.org/problems/combination-sum-ii-1664263832/1

#User function Template for python
    
class Solution:
    def dfs(self, arr, ind, k, ans, curr):
        """
        Depth-first search function to find combinations that sum up to k.

        Parameters:
        - arr: The input array of integers.
        - ind: The current index in the array.
        - k: The target sum.
        - ans: The list to store valid combinations.
        - curr: The list to store the current combination being explored.
        """
        # Base cases
        if k == 0:
            # If k is 0, we found a valid combination, append it to the answer list
            ans.append(curr[:])
            return
        if ind == len(arr) or k < 0:
            # If we reach the end of the array or k becomes negative, backtrack
            return

        # Explore combinations starting from the current index
        for i in range(ind, len(arr)):
            # Skip duplicates
            if i != ind and arr[i] == arr[i - 1]:
                continue
            # Include current element in the combination
            curr.append(arr[i])
            # Recursively search for combinations with reduced target sum
            self.dfs(arr, i + 1, k - arr[i], ans, curr)
            # Backtrack: remove the last element to explore other combinations
            curr.pop()

    def CombinationSum2(self, arr, n, k):
        """
        Main function to find combinations that sum up to k.

        Parameters:
        - arr: The input array of integers.
        - n: Length of the array (not used in this implementation).
        - k: The target sum.

        Returns:
        - ans: List of combinations that sum up to k.
        """
        # Initialize variables
        ans = []  # List to store valid combinations
        curr = []  # List to store the current combination being explored
        arr.sort()  # Sort the array to handle duplicates correctly
        # Call the DFS function to find combinations
        self.dfs(arr, 0, k, ans, curr)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ob = Solution()
    result = ob.CombinationSum2(arr, n, k)
    for row in result:
        print(*row)
    if not result:
        print()

# } Driver Code Ends