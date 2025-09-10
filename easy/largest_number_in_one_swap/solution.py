# Problem Statement: https://www.geeksforgeeks.org/problems/largest-number-in-one-swap1520/1

class Solution:
    def largestSwap(self, s):
        s = list(s)
        n = len(s)
        
        # Record the last occurrence of each digit
        last = [-1] * 10
        for i, ch in enumerate(s):
            last[int(ch)] = i
        
        # Try to swap current digit with a bigger digit on its right
        for i in range(n):
            for d in range(9, int(s[i]), -1):
                if last[d] > i:
                    # Swap and return the new string
                    s[i], s[last[d]] = s[last[d]], s[i]
                    return ''.join(s)
        
        return ''.join(s)  # no swap needed
