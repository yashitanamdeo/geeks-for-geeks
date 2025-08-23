# Problem Statement: https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

class Solution:
     def findPages(self, arr, k):
        n = len(arr)
        if n < k:
            return -1
        
        def check_if_possible(limit):
            curr_pages, groups = 0, 1
            for pages in arr:
                curr_pages += pages
                if curr_pages > limit:
                    curr_pages = pages
                    groups += 1
                    if groups > k:
                        return False
            return True
        
        lo, hi = max(arr), sum(arr)
        while lo < hi:
            guess = lo + (hi - lo) // 2
            if check_if_possible(guess):
                hi = guess
            else:
                lo = guess + 1
        return lo