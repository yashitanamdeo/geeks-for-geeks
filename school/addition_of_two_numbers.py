'''Problem Statement: https://practice.geeksforgeeks.org/problems/addition-of-two-numbers0812/1/?difficulty[]=-2&page=1&query=difficulty[]-2page1'''

#User function Template for python3
class Solution:
    def addition (ob,A,B):
        # code here 
        return A+B

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input())
    for _ in range (t):
        
        A,B=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.addition(A,B))
# } Driver Code Ends