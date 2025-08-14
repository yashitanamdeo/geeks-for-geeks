# Problem Statement: https://www.geeksforgeeks.org/problems/count-reverse-pairs/1

class Solution:
    def merge_sort(self, arr, start, end):
        if start == end:
            return 0, [arr[start]]
        mid = start + (end - start) // 2
        count_left, left = self.merge_sort(arr, start, mid)
        count_right, right = self.merge_sort(arr, mid + 1, end)
        count = count_left + count_right
        n, m = len(left), len(right)
        # Count the "reverse pairs"
        ri = 0
        for l in left:
            while ri < m and l > 2 * right[ri]:
                ri += 1
            count += ri
        tmp = []
        li = ri = 0
        while li < n and ri < m:
            if left[li] <= right[ri]:
                tmp.append(left[li])
                li += 1
            else:
                tmp.append(right[ri])
                ri += 1
        tmp.extend(left[li:])
        tmp.extend(right[ri:])
        return count, tmp
        
        
    def countRevPairs(self, arr):
        return self.merge_sort(arr, 0, len(arr) - 1)[0]