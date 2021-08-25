#User function Template for python3
import math

class Solution:
    def findRemainder(self, num1, num2):
        if num1 < num2:
            return num1
        else:
            return math.ceil(num1%num2)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        num1,num2 = map(int,input().strip().split())
        ob = Solution()
        print(ob.findRemainder(num1,num2))
# } Driver Code Ends