# Problem Statement: https://www.geeksforgeeks.org/problems/top-k-frequent-elements-in-array/1

class Solution:
    def topK(self, nums, k):

        dict = {}
        res = []

        # count the frequencies
        for x in nums:
            if x in dict.keys():
                dict[x] = dict[x]+1
            else:
                dict[x] = 1

        # short with respect to values, then with respect to keys
        d = sorted(dict.items(), key=lambda x: (x[1], x[0]), reverse=True)

        # get the first k items
        n = len(d)
        for i in range(min(n, k)):
            res.append(d[i][0])

        return res

# {
 # Driver Code Starts


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = list(map(int, input().strip().split()))
        n = a[0]
        nums = a[1:]
        k = int(input().strip())
        obj = Solution()
        ans = obj.topK(nums, k)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends
