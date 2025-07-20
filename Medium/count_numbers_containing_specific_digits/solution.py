# Problem Statement: https://www.geeksforgeeks.org/problems/count-numbers-containing-specific-digits/1

import math

class Solution:
    def countValid(self, n, arr):
        total_n_digits = 10 ** (n - 1) * 9
        step = 9 - len(arr)
        step += 1 if 0 in arr else 0
        non_numbers = step * (10 - len(arr)) ** (n - 1)
        return total_n_digits - non_numbers