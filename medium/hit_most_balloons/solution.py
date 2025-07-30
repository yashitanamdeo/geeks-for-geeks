# Problem Statement: https://practice.geeksforgeeks.org/problems/4e75764f8f1638eb4f1c5478ca1986043e15e39a/1

#User function Template for python3

class Solution: 
    def mostBalloons(self, N, arr):
        # Code here
        if N<3:
            return N

        max_val=0
        for i in arr:
            d = {}
            dups = 0
            cur_max = 0
            for j in arr:
                if i!=j:
                    if j[0]==i[0]:
                        slope='inf'
                    else:
                        slope=float(j[1]-i[1])/float(j[0]-i[0])
                    d[slope] = d.get(slope,0)+1
                    cur_max=max(cur_max, d[slope])
                else:
                    dups+=1
            max_val=max(max_val, cur_max+dups)
        return max_val

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input()) 
        arr=[[] for j in range(N)]
        for j in range(2): 
            inp = [int(i) for i in input().split()] 
            for i in range(N): 
                arr[i].append(inp[i])
        ob = Solution()
        print(ob.mostBalloons(N, arr))
        
        T -= 1
# } Driver Code Ends