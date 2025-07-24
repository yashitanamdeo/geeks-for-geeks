# Problem Statement: https://www.geeksforgeeks.org/problems/sum-of-bit-differences2937/1

#User function Template for python3
class Solution:
	def sumBitDifferences(self,arr, n):
	    l=[0]*(33)
	    ma=len(bin(max(arr))[2:])
	    for i in range (n):
    	    
    	    bi=bin(arr[i])[2:]
    	    bi=(ma-len(bi))*"0"+bi
    	    for j in range(ma):
    	        
    	        if(bi[j]=="1"):
    	            l[j]+=1
    	ans=0
    	
    	for i in l:
    	    ans+=i*(n-i)
    	return(ans*2)



#{ 
 # Driver Code Starts

#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumBitDifferences(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends