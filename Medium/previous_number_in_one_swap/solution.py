# Problem Statement: https://practice.geeksforgeeks.org/problems/previous-number-in-one-swap5707/1#

#User function Template for python3
class Solution:
   def lower_bound(ob,A,i):
       m = -1
       k = 0
       for j in range(i,len(A)):
           if A[i-1] > A[j]:
               if m < int(A[j]):
                   m = int(A[j])
                   k = j
       return k
   def previousNumber(ob,S):
       # code here 
       A = list(S)
       t = 0
       d = 0
       for i in range(len(S)-1,0,-1):
           if A[i] < A[i-1]:
               t = ob.lower_bound(A,i)
               A[t],A[i-1] = A[i-1],A[t]
               break
       r = ''.join(A)
       if S == r or r[0] == '0':
           return -1
       else:
           return r
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.previousNumber(S))
# } Driver Code Ends