# Problem Statement: https://practice.geeksforgeeks.org/problems/handshakes1303/1

#User function Template for python3

class Solution:
    def count(self, N):
        result=0
        if(N%2==1):
            return 0
        elif(N==0):
            return 1
        for i in range(0,N,2):
            result+=self.count(i)*self.count(N-2-i)
        return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.count(N))
# } Driver Code Ends