# Problem Statement: https://www.geeksforgeeks.org/problems/make-matrix-beautiful-1587115620/1

class Solution:
    def balanceSums(self, mat):
        row_max = max([ sum(arr) for arr in mat ])
        col_max = max([ sum(arr) for arr in zip(*mat) ])
        target_sum = max(row_max, col_max)
        return sum(target_sum - sum(arr) for arr in mat)