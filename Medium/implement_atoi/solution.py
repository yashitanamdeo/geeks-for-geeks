# Problem Statement: https://www.geeksforgeeks.org/problems/implement-atoi/1

#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        d={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        ans=0
        if s[0]=='-':
            i=1
        else:
            i=0
        while i<len(s):
            if s[i] in d:
                ans+=d[s[i]]
                if i+1!=len(s):
                    ans*=10
                i+=1
            else:
                return -1
            
        if s[0]=='-':
            return -ans
        else:
            return ans


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends