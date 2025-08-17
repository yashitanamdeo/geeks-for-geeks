# Problem Statement: https://www.geeksforgeeks.org/problems/sort-by-absolute-difference-1587115621/1

class Solution:
    def rearrange(self, arr, x):
        return arr.sort(key = lambda k : abs(k-x))
