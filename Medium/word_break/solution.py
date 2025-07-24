# Problem Statement: https://www.geeksforgeeks.org/problems/word-break1352/1

#User function Template for python3

class Solution:
    def wordBreak(self, n, s, d):
        def solve(s):
            if not s:
                return True
            for i in d:
                if s.startswith(i) and solve(s[len(i):]):
                    return True
            return False
        return solve(s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends