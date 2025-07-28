# Problem Statement: https://www.geeksforgeeks.org/problems/count-the-coprimes/1

from collections import defaultdict
from math import sqrt, prod
class Solution:
    def cntCoprime(self, arr):
        def factorize(num):
            res = []
            for i in range(2, int(sqrt(num))+1):
                if num%i == 0:
                    while num%i == 0:
                        num //= i
                    res.append(i)
            if num > 1:
                res.append(num)
            return res
        
        n = len(arr)
        sign, count = dict(), defaultdict(int) 
        for a in arr:
            factors = factorize(a)
            m = len(factors)
            for mask in range(1, 1<<m):
                sub = prod(factors[i] for i in range(m) if mask&(1<<i))
                count[sub] += 1
                sign[sub] = 1 if mask.bit_count()%2 else -1
        
        invalid = sum(count[x]*(count[x]-1)//2 * sign[x] for x in count)
        return n*(n-1)//2 - invalid