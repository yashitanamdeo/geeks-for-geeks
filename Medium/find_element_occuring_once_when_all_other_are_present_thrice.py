# Problem Statement: https://www.geeksforgeeks.org/problems/find-element-occuring-once-when-all-other-are-present-thrice/1

# User function Template for python3

class Solution:
    def singleElement(self, arr, N):
        # code here
        hashmap = {}
        for i in range(N):
            if arr[i] not in hashmap:
                hashmap[arr[i]] = 1
            else:
                hashmap[arr[i]] += 1
        key = list(hashmap.keys())
        val = list(hashmap.values())
        return key[val.index(1)]


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        print(ob.singleElement(arr, N))
# } Driver Code Ends
