# Problem Statement: https://www.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1

class Solution:
    def smallestWindow(self, s, p):
        from collections import Counter
        
        # Step 1: Frequency of characters in p
        need = Counter(p)
        need_count = len(need)  # how many distinct characters we need
        have = 0
        window = {}
        
        res, res_len = [-1, -1], float("inf")
        left = 0

        # Step 2: Expand window with right pointer
        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            # Step 3: Shrink from left if valid
            while have == need_count:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""