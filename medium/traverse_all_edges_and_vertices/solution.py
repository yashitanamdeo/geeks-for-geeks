# Problem Statement: https://www.geeksforgeeks.org/problems/castle-run3644/1

#User function Template for python3

def areAllVerticesEvenDegree(paths):
    for path in paths:
        if sum(path) % 2 != 0:
            return False
    return True
        
class Solution:
	def isPossible(self, paths):
		return int(areAllVerticesEvenDegree(paths))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		paths = []
		for _ in range(n):
			cur = list(map(int, input().split()))
			paths.append(cur)
		obj = Solution()
		ans = obj.isPossible(paths)
		print(ans)

# } Driver Code Ends