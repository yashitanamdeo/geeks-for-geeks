# Problem Statement: https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        n=len(s)
        ans=-1
        left=0
        map={}
        for right in range(n):
            if s[right] in map:
                map[s[right]]+=1
            else:
                map[s[right]]=1
            while len(map)>k:
                map[s[left]]-=1
                if map[s[left]]==0:
                    del map[s[left]]
                left+=1
            
            if len(map)==k:
                ans=max(ans, right-left+1)

        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends