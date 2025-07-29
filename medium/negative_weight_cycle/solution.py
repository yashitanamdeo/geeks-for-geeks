# Problem Statement: https://www.geeksforgeeks.org/problems/negative-weight-cycle3504/1

#User function Template for python3

class Solution:
	def isNegativeWeightCycle(self, n, edges):
    	
        dist = [float("inf")]*n
       	dist[0] = 0
    	
       	for i in range(n-1):
            updated = False
            for u,v,w in edges:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                	updated = True
        	if not updated:
                return 0
   	
       	for u,v,w in edges:
           	if dist[v] > dist[u] + w:
               	return 1
                	
       	return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		edges = []
		for _ in range(m):
			edges.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.isNegativeWeightCycle(n, edges)
		print(ans)

# } Driver Code Ends