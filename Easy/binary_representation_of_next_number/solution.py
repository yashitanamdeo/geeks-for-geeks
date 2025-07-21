# Problem Statement: https://www.geeksforgeeks.org/problems/binary-representation-of-next-number3648/1

#User function Template for python3
class Solution:
	def binaryNextNumber(self, s):
        s=s.lstrip("0")
        n,cry,ans=len(s),1,""
        for i in range(n-1,-1,-1):
            bit= int(s[i])
            val=bit+cry
            ans=str(val%2)+ans
            cry=val//2
        return "1"+ans if cry else ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        ans = ob.binaryNextNumber(S)
        print(ans)

# } Driver Code Ends