# Problem Statement: https://practice.geeksforgeeks.org/problems/5551749efa02ae36b6fdb3034a7810e84bd4c1a4/1

#User function Template for python3

class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):
        # code here
        unvis = 0
        vis = [False]*(leaves+1)
        for i in range(N):
            curr = frogs[i]
            if curr <= leaves and vis[curr] == False:
                for j in range(curr, leaves+1, curr):
                    vis[j] = True
        for i in range(1, leaves+1):
            if vis[i] == False:
                unvis += 1
        return unvis


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        N, leaves = [int(i) for i in input().split()]
        frogs = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.unvisitedLeaves(N, leaves, frogs))

        T -= 1
# } Driver Code Ends
