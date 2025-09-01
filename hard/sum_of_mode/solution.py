# Problem Statement: https://www.geeksforgeeks.org/problems/sum-of-mode/1

from collections import Counter
from heapq import heapify, heappush, heappop
        
class Solution:
     def sumOfModes(self, arr, k):
        if k == 1:
            return sum(arr)
        n = len(arr)
        freqs = Counter(arr[:k])
        h = [(-count, a) for a, count in freqs.items()]
        heapify(h)
        modes_sum = h[0][1]
        for i in range(k, n):
            first, last = arr[i - k], arr[i]
            freqs[first] -= 1
            freqs[last] += 1
            heappush(h, (-freqs[first], first))
            heappush(h, (-freqs[last], last))
            while -h[0][0] != freqs[h[0][1]]:
                heappop(h)
            modes_sum += h[0][1]
        return modes_sum

