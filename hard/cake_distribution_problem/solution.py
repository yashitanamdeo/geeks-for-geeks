# Problem Statement: https://practice.geeksforgeeks.org/problems/0a7c7f1089932257071f9fa076f25d353f91e0fd/1

#User function Template for python3

class Solution():
    def maxSweetness(self, sweetness, n, k):
        #your code goes here
        def isPossible(sw, k, mid):
            count = 0
            summ = 0
            for x in sw:
                summ += x
                if summ >= mid:
                    count += 1
                    summ = 0
            return count >= k+1

        high = sum(sweetness)
        low = min(sweetness)

        mid = 0
        while low <= high:
            mid = (low+high)//2
            if isPossible(sweetness, k, mid):
                low = mid+1
            else:
                high = mid-1

        return low-1


#{
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n, k = map(int, input().split())
    sweetness = [int(i) for i in input().split()]
    print(Solution().maxSweetness(sweetness, n, k))
# } Driver Code Ends
