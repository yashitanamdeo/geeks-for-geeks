# Problem Statement: https://practice.geeksforgeeks.org/problems/binary-array-sorting-1587115620/1#

#User function Template for python3

class Solution:
    
    #Function to sort the binary array.
    def binSort(self, A, N): 
        #Your code here
        #No need to print the array
        return A.sort() # simple inbuilt method to sort array/list
'''
    def binSort(self, A, N): 
            #Your code here
            #No need to print the array
            j = 0
            for i in range(N):
                if A[i]==0: # agar 1 hai toh hum i ki value badhne denge jab tak i 0 nhi hojata
                    A[i],A[j] = A[j],A[i] # jab i 0 hojayega tab hum A[j] ki value se swap/replace kardenge because woh hamesha 1 hi rehega 
                    j += 1 # jab hum replace karenge tab hi j ko agey badhayenge
            return A
'''
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=list(map(int,input().split()))
            obj = Solution()
            obj.binSort(A,N)
            
            for i in A:
                print(i,end=" ")
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends