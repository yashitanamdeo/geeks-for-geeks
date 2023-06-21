# Problem Statement: https://practice.geeksforgeeks.org/problems/reverse-coding2452/1

#User function Template for python3

class Solution:
    def sumOfNaturals(self, n):
        # code here
        return (n*(n+1)//2)%(10**9+7)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.sumOfNaturals(n))
# } Driver Code Ends
