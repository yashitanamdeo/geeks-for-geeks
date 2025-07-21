# Problem Statement: https://practice.geeksforgeeks.org/problems/ticket-counter-2731/1

class Solution:
    def distributeTicket(self, N: int, k: int) -> int:
        # Code Here
        l = 1
        h = N
        flag = True
        while l < h:
            if flag:
                if l+k > h:
                    l = h
                else:
                    l += k
                flag = False
            else:
                if h-k < l:
                    h = l
                else:
                    h -= k
                flag = True
        return l


# {
 # Driver Code Starts
t = int(input())
for _ in range(t):

    N, K = map(int, input().split())

    obj = Solution()
    res = obj.distributeTicket(N, K)

    print(res)
# } Driver Code Ends
