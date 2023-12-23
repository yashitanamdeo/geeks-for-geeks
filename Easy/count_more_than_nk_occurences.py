# Problem Statement: https://www.geeksforgeeks.org/problems/count-element-occurences/1

#User function Template for python3


from collections import defaultdict

class Solution:
    def countOccurence(self, A, N, K):
        mp = defaultdict(int)
        ans = 0
        for i in range(N):
            mp[A[i]] += 1
        for key, value in mp.items():
            if value > N // K:
                ans += 1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(Solution().countOccurence(A, N, K))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends