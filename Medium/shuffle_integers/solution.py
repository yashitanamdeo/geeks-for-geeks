# Problem Statement: https://www.geeksforgeeks.org/problems/shuffle-integers2401/1

class Solution:
    def shuffleArray(self, arr, n):
        for i in range(0, n//2):
            arr[2*i] += ((arr[i] % 1001)*1001)
        for i in range(n//2, n):
            ind = i-(n//2)
            arr[2*ind+1] += ((arr[i] % 1001)*1001)
        for i in range(n):
            arr[i] //= 1001


# {
 # Driver Code Starts
if __name__ == '__main__':

    t = int(input())
    for _ in range(0, t):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        ob.shuffleArray(a, n)
        print(*a)
# } Driver Code Ends
