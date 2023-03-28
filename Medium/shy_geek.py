# Problem Statement: https://practice.geeksforgeeks.org/problems/59dfb26eb6c659e6e5f60869ac335f450f97165a/1

#{
# Driver Code Starts
#Initial Template for Python 3

class Shop:
    chocolates = []
    countOfCalls = 0

    def __init__(self):
        self.chocolates = []
        self.countOfCalls = 0

    def addChocolate(self, price):
        self.chocolates.append(price)

    def get(self, i):
        self.countOfCalls += 1
        if (self.countOfCalls > 50 or i >= len(self.chocolates) or i < 0):
            return -1
        return self.chocolates[i]


# } Driver Code Ends
#User function Template for python3

"""
Instructions - 

    1. 'shop' is object of class Shop.
    2. User 'shop.get(int i)' to enquire about the price
            of the i^th chocolate.
    3. Every chocolate in shop is arranged in increasing order
            i.e. shop.get(i) <= shop.get(i + 1) for all 0 <= i < n - 1
"""


class Solution:
    def __init__(self, s):
        self.shop = s

    def find(self, n, k):
        ans = 0
        l = 0
        r = n - 1
        while r >= 0 and k > 0:
            l = 0
            index = -1
            index_val = 0
            while l <= r:
                mid = (l + r) // 2
                mid_price = self.shop.get(mid)
                if mid_price <= k:
                    index = mid
                    index_val = mid_price
                    l = mid + 1
                else:
                    r = mid - 1
            if index_val == 0:
                break
            ans += (k // index_val)
            k = k % index_val
            r = index - 1
        return ans

#{
 # Driver Code Starts.


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        shop = Shop()
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        for choco in arr:
            shop.addChocolate(choco)
        ob = Solution(shop)
        ans = ob.find(n, k)
        print(ans)
        tc -= 1


# } Driver Code Ends
