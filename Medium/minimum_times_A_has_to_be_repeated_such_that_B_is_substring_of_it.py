# Problem Statement: https://practice.geeksforgeeks.org/problems/5ef42ba605fff6cd60b1b2dd2ee230ade1fa25b0/1#

#User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        # code here 
        dummy = A
        for i in range(1,10**3): #acc. to constraints it cannot repeat more than 10**3 times
            if B in dummy:
                return i
            dummy += A
        return -1
        '''
        check if B is present in A - if it is then return the number of times
        loop ran in order to return minimum number of repetitions of string A 
        else if it doesn't return therefore B cannot be a substring of A in any case so return -1
        '''
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A=input()
        B=input()
        
        ob = Solution()
        print(ob.minRepeats(A,B))
# } Driver Code Ends