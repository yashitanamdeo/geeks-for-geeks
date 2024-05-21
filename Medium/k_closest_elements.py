# Problem Statement: https://www.geeksforgeeks.org/problems/k-closest-elements3619/1

#User function Template for python3

class Solution:
    def printKClosest(self, arr, n, k, x):
        # code here
        if x not in arr:
            arr.append(x)
            arr = sorted(arr)
            n += 1
        res = []
        ind = arr.index(x)
        left = ind - 1
        right = ind + 1
        req = k
        while k:
            if right == n and left == -1:
                break
            elif right == n or (left > -1 and x - arr[left] < arr[right] - x):
                res.append(arr[left])
                left -= 1
            elif left == -1 or (right < n and arr[right] - x <= x - arr[left]):
                res.append(arr[right])
                right += 1
            k -= 1
        return res + [0] * (req - len(res))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k, x = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printKClosest(arr, n, k, x)
        for xx in ans:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends