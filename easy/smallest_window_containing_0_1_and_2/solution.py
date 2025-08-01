# Problem Statement: https://www.geeksforgeeks.org/problems/smallest-window-containing-0-1-and-2--170637/1

# User function Template for python3

class Solution:
    def smallestSubstring(self, S):

        # initialization
        i = 0
        j = 3
        res = -1

        # main loop with index updates
        while j <= len(S):
            st = S[i:j]
            if ("0" in st) and ("1" in st) and ("2" in st):
                if res == -1:
                    res = len(st)
                else:
                    res = min(res, len(st))
                i += 1
            else:
                j += 1

        return res

class Solution2:
    def smallestSubstring(self, S):
           
        lstind = [-1,-1,-1]
        ans = 1000000
       
        for index, item in enumerate(S):
            lstind[int(item)] = index+1
            if -1 not in lstind:

                ans = min(ans, max(lstind)- min(lstind))
       
        if ans == 1000000:
            return -1
        return ans + 1
    
# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.smallestSubstring(S)

        print(ans)


# } Driver Code Ends
