# Problem Statement: https://www.geeksforgeeks.org/problems/remove-all-duplicates-from-a-given-string4321/1

#User function Template for python3
class Solution:
	def removeDuplicates(self,str):
	    string=''
	    s=set(str)
	    for i in str:
	        if i in s:
	            string+=i
	            s.remove(i)
	    return string


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        str = input().strip()
        ob = Solution()
        ans = ob.removeDuplicates(str)
        print(ans)
        tc -= 1

# } Driver Code Ends