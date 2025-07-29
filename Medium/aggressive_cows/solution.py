# Problem Statement: https://practice.geeksforgeeks.org/problems/aggressive-cows/1

#User function Template for python3

class Solution:
    def solve(self, n, k, arr):
        arr.sort()
        low = 0
        high = arr[n-1]-arr[0]
        res = []
        while low <= high:
            mid = low+high >> 1
            if self.cow_Place(arr, n, k, mid):
                res.append(mid)
                low = mid+1
            else:
                high = mid-1
        return max(res)

    def cow_Place(self, arr, n, k, mid):
        coor = arr[0]
        count = 1
        for i in range(1, n):
            if arr[i]-coor >= mid:
                count += 1
                coor = arr[i]
            if count == k:
                return True
        return False


#{
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
