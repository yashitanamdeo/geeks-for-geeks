# Problem Statement: https://www.geeksforgeeks.org/problems/shortest-path-from-1-to-n0156/1

#User function Template for python3

class Solution:
    def minimumStep (self, n):
        #complete the function here
        if n == 1:
            return 0
        if n%3 == 0:
            return 1 + self.minimumStep(n/3)
        else:
            return 1 + self.minimumStep(n-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        print(ob.minimumStep(n))
# } Driver Code Ends