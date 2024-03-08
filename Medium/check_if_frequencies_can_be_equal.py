# Problem Statement: https://www.geeksforgeeks.org/problems/check-frequencies4211/1

#User function Template for python3
from collections import Counter

class Solution:
    def sameFreq(self, s: str) -> bool:
        freq = Counter(s)
        values = list(freq.values())
        distinct_values = set(values)
        
        if len(distinct_values) == 1:
            return True  # All characters have the same frequency already
        
        if len(distinct_values) == 2:
            # Check if it's possible to remove one character
            min_freq, max_freq = min(distinct_values), max(distinct_values)
            if values.count(min_freq) == 1 and min_freq == 1:
                return True
            if values.count(max_freq) == 1 and max_freq - min_freq == 1:
                return True
        
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends