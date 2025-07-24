# Problem Statement: https://practice.geeksforgeeks.org/problems/satisfy-the-equation5847/1

#User function Template for python3

class Solution:
    def satisfyEqn(self, A, N):
        # code here 
        mp = {}
        ans = [999, 999, 999, 999]
        temp = [None]
        for i in range(N):
            for j in range(i+1, N):
                if (A[i]+A[j]) not in mp:
                    mp[A[i] + A[j]] = i, j
                else:
                    temp[0] = mp[A[i] + A[j]]
                    a, b, c, d = temp[0][0], temp[0][1], i, j
                    if a == c or a == d or b == c or b == d:
                        continue
                    elif a < ans[0]:
                        ans[0], ans[1], ans[2], ans[3] = a, b, c, d
                    elif a == ans[0]:
                        if b < ans[1]:
                            ans[0], ans[1], ans[2], ans[3] = a, b, c, d
                        elif b == ans[1]:
                            if c < ans[2]:
                                ans[0], ans[1], ans[2], ans[3] = a, b, c, d
                            elif c == ans[2]:
                                if d < ans[3]:
                                    ans[0], ans[1], ans[2], ans[3] = a, b, c, d
                                else:
                                    continue
        if ans == [999, 999, 999, 999]:
            ans = [-1, -1, -1, -1]
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A=list(map(int,input().split()))
        
        ob = Solution()
        ptr=ob.satisfyEqn(A,N)
        print(*ptr)
# } Driver Code Ends