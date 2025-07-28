# Problem Statement: https://www.geeksforgeeks.org/problems/divisible-by-13/1

class Solution:
    def divby13(self, s):
        curr_num = 0
        ord_0 = ord("0")
        for c in reversed(s):
            curr_num += ord(c) - ord_0
            curr_num, r = divmod(curr_num, 10)
            curr_num += 4 * r
            curr_num %= 13
        return curr_num == 0