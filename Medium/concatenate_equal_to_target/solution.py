# Problem Statement: https://practice.geeksforgeeks.org/problems/1df2447c003940512562d766cf0583bbdc7a75ed/1

#User function Template for python3
class Solution:
    def countPairs(self, N, X, arr): 
        #code here
        count=0
        dic={}
        for i in arr:
            if str(i) in dic:
                dic[str(i)]+=1
            else:
                dic[str(i)]=1
        # print(dic)
       
        no=str(X)
        for i in range(len(no)):
            s1=no[:i+1]
            s2=no[i+1:]
           
            if s1 in dic and s2 in dic:
                if s1==s2:
                    count+=(dic[s1]*(dic[s2]-1))
                else:
                    count+=(dic[s1]*dic[s2])
                   
        return count
       
#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        numbers = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countPairs(N, X, numbers)
        print(ans)


# } Driver Code Ends