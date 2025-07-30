# Problem Statement: https://practice.geeksforgeeks.org/problems/substrings-of-length-k-with-k-1-distinct-elements/1

#User function Template for python3

class Solution:
    def countOfSubstrings(self, S, K):
        result = 0
        hash = {}
        
        for i in range(K):
            hash[S[i]] = hash.get(S[i], 0) + 1
        if len(hash) == K-1:
            result += 1
            
        for i in range(K, len(S)):
            hash[S[i]] = hash.get(S[i], 0) + 1
            
            if hash[S[i - K]] == 1:
                hash.pop(S[i - K])
            else:
                hash[S[i - K]] -= 1
                
            if len(hash) == K-1:
                result += 1
                
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        K=int(input())
        
        ob = Solution()
        print(ob.countOfSubstrings(S,K))
# } Driver Code Ends