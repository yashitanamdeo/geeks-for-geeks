# Problem Statement: https://www.geeksforgeeks.org/problems/find-duplicate-rows-in-a-binary-matrix/1

# User function Template for python3

class Solution:
    def repeatedRows(self, arr, m, n):
        # code here
        ans = []
        hash = dict()
        for i in range(m):
            temp = ""
            for j in range(n):
                temp += str(arr[i][j])
            if temp in hash:
                hash[temp] += 1
                ans.append(i)
            else:
                hash[temp] = 1
        return ans


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))

        arr = []
        for i in range(n):
            nums = list(map(int, input().strip().split()))
            arr.append(nums)
        ob = Solution()
        ans = ob.repeatedRows(arr, n, m)

        for x in ans:
            print(x, end=" ")

        print()
        tc -= 1

# } Driver Code Ends
