# Problem Statement: https://practice.geeksforgeeks.org/problems/swap-bits5726/1#

#User function Template for python3

class Solution:
   def swapBits(self, X, P1, P2, N):
       j = bin(X)[2:].zfill(32)
       swap1 = j[-(P1+1):-(P1+1+N):-1] 
       swap2 = j[-(P2+1):-(P2+1+N):-1]
       s1 = swap1[::-1]
       s2 = swap2[::-1]
       result = eval('0b'+j[0:(len(j)-P2-N)]+s1+j[len(j)-P2:(len(j)-P1-N)]+s2+j[len(j)-P1:])
       return result


#{ 
#  Driver Code Starts

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        obj = Solution()
        X, P1, P2, N = map(int, input().split())
        print(obj.swapBits(X, P1, P2, N))
        

# } Driver Code Ends