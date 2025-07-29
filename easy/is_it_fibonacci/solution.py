# Problem Statement: https://practice.geeksforgeeks.org/problems/202d95ecdeec659401edc63dd952b1d37b989ab8/1

#User function Template for python3

class Solution():
    def solve(self, N, K, GeekNum):
        #your code goes here
        for i in range(N-len(GeekNum)):
            GeekNum.append(sum(GeekNum[i:K+1+i]))
        return GeekNum[-1]


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N, K = map(int, input().split())
        GeekNum = [int(i) for i in input().split()]
        print(Solution().solve(N, K, GeekNum))


# } Driver Code Ends
