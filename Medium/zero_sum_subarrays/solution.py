# Problem Statement: https://practice.geeksforgeeks.org/problems/zero-sum-subarrays1825/1

# User function Template for python3

class Solution:
    # Function to count subarrays with sum equal to 0.
    def findSubArrays(self, arr, n):

        # return: count of sub-arrays having their sum equal to 0
        if n == 1:
            if arr[0] == 0:
                return 1
            else:
                return 0
        su = 0
        dic = {}
        dic[0] = 1
        count = 0
        for ele in arr:
            su += ele
            if su in dic:
                if dic[su] > 1:
                    count += dic[su]
                else:
                    count += 1
                dic[su] += 1
            else:
                dic[su] = 1
        return count

# {
 # Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB


if __name__ == '__main__':
    t = int(input())
    for tc in range(t):

        N = int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A, N))


# } Driver Code Ends
