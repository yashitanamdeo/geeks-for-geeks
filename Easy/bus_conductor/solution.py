# Problem Statement: https://practice.geeksforgeeks.org/problems/c6ced401352fd126b89129cd562a9247f057e40e/1

# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3

class Solution:
    def findMoves(self, n, chairs, passengers):
        # code here
        chairs.sort()
        passengers.sort()
        count = 0
        for i in range(n):
            count += abs(passengers[i]-chairs[i])
        return count


# {
 # Driver Code Starts.
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        obj = Solution()
        print(obj.findMoves(n, a, b))

# } Driver Code Ends
