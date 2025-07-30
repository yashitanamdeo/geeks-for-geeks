# Problem Statement: https://practice.geeksforgeeks.org/problems/5c2734730cb1e98e3877a0b91f7d680d0efc8acf/1

#User function Template for python3

class Solution:
    def secondSmallest(self, S, D):
        if S >= D * 9:
            return -1
        ans = [0 for i in range(D)]
        ans[0] = 1
        S -= 1
        D -= 1
        ind = len(ans) - 1
        for i in range(len(ans) - 1, -1, -1):
            if S >= 9:
                ans[i]+= 9
                S -= 9
                ind = i
            else:
                ans[i]+= S
                S = 0

        ans[ind] = ans[ind] - 1
        ans[ind - 1] = ans[ind - 1] + 1
        return int("".join(map(str, ans)))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,D=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.secondSmallest(S,D))
# } Driver Code Ends