# Problem Statement: https://www.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1

#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        
        m={}
        prefix=0
        for j,i in enumerate(arr):
            if i==0:
                return 1
                
            if prefix in m:
                return 1
                
            if prefix not in m:
                m[prefix]=j
                
            prefix+=i
            
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends