# Problem Statement: https://practice.geeksforgeeks.org/problems/excel-sheet5448/1#

#User function Template for python3

class Solution:
    def ExcelColumn(self, N):
        #return required string
        #code here
        ans = ''
        while(N > 0):
            rem = N % 26
            if(rem == 0):
                ans += 'Z'
                N = N//26 - 1
            else:
                ans += chr(rem+64)
                N = N//26
        return ans[::-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        ob=Solution()
        print(ob.ExcelColumn(n))

# } Driver Code Ends