# Problem Statement: https://www.geeksforgeeks.org/problems/minimum-number-of-k-consecutive-bit-flips--171650/1

class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        isFlipped = [0] * n
        flipped = 0
        ans = 0

        for i in range(n):
            # Remove flip effect outside the window
            if i >= k:
                flipped ^= isFlipped[i - k]

            # If current bit is 0 after considering flips → need a flip here
            if arr[i] ^ flipped == 0:
                if i + k > n:  # can't flip, out of bounds
                    return -1
                isFlipped[i] = 1
                flipped ^= 1
                ans += 1

        return ans