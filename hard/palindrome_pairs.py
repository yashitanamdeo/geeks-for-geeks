# Problem Statement: https://practice.geeksforgeeks.org/problems/palindrome-pairs/1#

#User function Template for python3

class Solution:
    def palindromepair(self, N, arr):
        if N <= 1:
            return 0
           
        d = {} #hashmap to store reverse of all strings and index
           
        for i in range(N):
            d[arr[i][::-1]] = i
               
        for i in range(N):
            x = arr[i]
               
            for j in range(len(x) + 1):
                pre = x[:j]
                suf = x[j:]
                if pre == pre[::-1]:
                    if suf in d:
                        if d[suf] != i:
                            return 1
                           
                if suf == suf[::-1]:
                    if pre in d:
                        if d[pre] != i:
                            return 1
        return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=[]
        for i in range(N):
            s = input()
            arr.append(s)
        
        ob = Solution()
        print(ob.palindromepair(N,arr))
# } Driver Code Ends