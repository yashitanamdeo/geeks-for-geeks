# Problem Statement: https://practice.geeksforgeeks.org/problems/unique-partitions1041/1

#User function Template for python3

class Solution:
    def UniquePartitions(self, n):
        dp = {1: ((1,),)}

        def recur(num):
            for i in range(2, num+1):
                cur = [[i]]
                for j in range(1, (i//2)+1):
                    for k in dp[i-j]:
                        cur.append(sorted(list(k)+[j], reverse=True))
                dp[i] = tuple(set(map(tuple, cur)))
        recur(n)

        return sorted(dp[n], reverse=True)


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T = int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.UniquePartitions(n)
		for a in ans:
			for b in a:
				print(b, end=" ")
		print()

# } Driver Code Ends
