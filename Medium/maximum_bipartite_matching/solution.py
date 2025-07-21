# Problem Statement: https://practice.geeksforgeeks.org/problems/9a88fe7ada1c49c2b3da7a67b43875e4a76aface/1

#User function Template for python3

class Solution:
	def maximumMatch(self, G):

		matched = [-1]*len(G[0])
		ans = 0

		def dfs(u, visited):
		    for i, v in enumerate(G[u]):
		        if v == 1 and i not in visited:
		            visited.add(i)
    		        if matched[i] == -1 or dfs(matched[i], visited):
    		            matched[i] = u
    		            return True
		    return False

	    for u, _ in enumerate(G):
	        if dfs(u, set()):
	            ans += 1
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m, n = map(int, input().strip().split())
		G = []
		for i in range(m):
			G.append(list(map(int, input().strip().split())))
		obj = Solution()
		ans = obj.maximumMatch(G)
		print(ans)
# } Driver Code Ends
