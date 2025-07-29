# Problem Statement: https://practice.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1

#User function Template for python3

class Solution:
    def minPartition(self, N):
        l = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
         s = []
          i = 9
           while(N):
                while(l[i] > N):
                    i -= 1
                s.append(l[i])
                N = N - l[i]
            return s


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends
