# Problem Statement: https://practice.geeksforgeeks.org/problems/wine-buying-and-selling/1

#User function Template for python3


class Solution:	
	def wineSelling(self, Arr, N):
		# code here
		ret = 0;
		Arr[1] += Arr[0]
		ret += abs(Arr[0])
		
		for i in range(1, N-1):
		    Arr[i+1] += Arr[i]
		    ret += abs(Arr[i])
		   
        return ret


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        Arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.wineSelling(Arr,N)
        
        print(ans)

# } Driver Code Ends