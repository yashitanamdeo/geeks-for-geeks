# Problem Statement: https://practice.geeksforgeeks.org/problems/8dcd25918295847b4ced54055eae35a8501181c1/1#

#User function Template for python3

class Solution:
    def search(self, patt, s):
        # code here
        ans = []
        for i in range(len(s)-len(patt)+1):
            if s[i:i+len(patt)] == patt:
                ans.append(i+1)
        return ans
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans)==0:
            print("-1", end = " ")
        else:
            for value in ans:
                print(value,end = ' ')
        print()
# } Driver Code Ends