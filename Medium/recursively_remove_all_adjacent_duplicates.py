# Problem Statement: https://practice.geeksforgeeks.org/problems/recursively-remove-all-adjacent-duplicates0744/1

#User function Template for python3

class Solution:
   def remove (self, S):
		if len(S)==1:
		    return S
	    news,flag="",False
	    for i in range(0,len(S)-1):
	        if S[i]!=S[i+1]:
	            if (i>0 and S[i-1]!=S[i]) or i==0:
	                news+=S[i]
	            if i==len(S)-2:  #when last char is unique
	                news+=S[i+1]
	            continue
	        
	        flag=True
	    if flag:
	        return self.remove(news)
	    else:
	        return news
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.remove(S))


# } Driver Code Ends