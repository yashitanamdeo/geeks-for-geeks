# Problem Statement: https://practice.geeksforgeeks.org/problems/63c232252d445a377e01cd91adfd7d1060580038/1

#User function Template for python3

class Solution:
    def maxIntersections(self, lines, N):
        # Code here
        l1 = []
        l2 = []
        for p in lines:
            l1.append(p[0])
            l2.append(p[1])
        l1.sort()
        l2.sort()
        i = 0
        j = 0
        ans = 0
        k = 0

        while(i < N and j < N):
            if(l1[i] <= l2[j]):
                k += 1
                ans = max(ans, k)
                i += 1
            else:
                k -= 1
                j += 1

        return ans


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        N = int(input())
        lines = [[] for j in range(N)]
        for j in range(2):
            prr = [int(i) for i in input().split()]
            for i in range(N):
                lines[i].append(prr[i])

        ob = Solution()
        print(ob.maxIntersections(lines, N))

        T -= 1

# } Driver Code Ends
