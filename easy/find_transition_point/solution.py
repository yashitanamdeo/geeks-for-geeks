# Problem Statement: https://www.geeksforgeeks.org/problems/find-transition-point-1587115620/1

class Solution:
    def transitionPoint(self, arr, n):
        l, h = 0, n-1
        while l < h:
            mid = (l+h)//2
            if arr[mid] > 0:
                h = mid
            else:
                l = mid+1
        return h if arr[h] == 1 else -1


# {
 # Driver Code Starts
# driver code
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.transitionPoint(arr, n))

# } Driver Code Ends
