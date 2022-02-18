# Problem Statement: https://practice.geeksforgeeks.org/problems/47e5aa3f32aee9e0405f04960f37c8a562d96a2f/1

#User function Template for python3

class Solution:
    def prank(self, a, n): 
       #code here
        for i in range(n):
            a[i] = a[i] + (a[a[i]]%n)*n
        for i in range(n):
            a[i]//=n

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        ob.prank(a, n)
        for i in a:
            print(i,end=" ")
        print()
# } Driver Code Ends