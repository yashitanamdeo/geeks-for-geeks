# Problem Statement: https://www.geeksforgeeks.org/problems/winner-of-an-election-where-votes-are-represented-as-candidate-names-1587115621/1

# User function Template for python3
from collections import OrderedDict


class Solution:

    # Complete this function

    # Function to return the name of candidate that received maximum votes.
    def winner(self, arr, n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        sol = []
        dict1 = {}
        for name in arr:
            if name in dict1:
                dict1[name] += 1
            else:
                dict1[name] = 1

        dict1 = OrderedDict(sorted(dict1.items()))
        res = max(dict1, key=lambda x: dict1[x])
        sol.append(res)
        sol.append(dict1[res])
        return sol


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):

        n = int(input())
        arr = input().strip().split()

        result = Solution().winner(arr, n)
        print(result[0], result[1])
# } Driver Code Ends
