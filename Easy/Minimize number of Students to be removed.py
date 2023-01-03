# Problem Statement: https://practice.geeksforgeeks.org/problems/7d0fa4007b8eabadc404fcc9fa917aa52982aa96/1


#User function Template for python3
from bisect import bisect_left

class Solution:
    def removeStudents(self, H, N):
        res = [H[0]]
        
        for i in range(1, N):
            if H[i] > res[-1]:
                res.append(H[i])
            
            else:
                res[bisect_left(res, H[i])] = H[i]
        
        return N - len(res)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        H=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.removeStudents(H,N))
# } Driver Code Ends
