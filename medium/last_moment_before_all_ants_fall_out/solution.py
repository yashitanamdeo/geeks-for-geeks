# Problem Statement: https://www.geeksforgeeks.org/problems/last-moment-before-all-ants-fall-out-of-a-plank/1

class Solution:
    def getLastMoment(self, n, left, right):
        # If 'left' is not empty, max time is the furthest left ant's position
        max_left = max(left) if left else 0
        
        # If 'right' is not empty, max time is the max(n - pos)
        max_right = max((n - r for r in right), default=0)
        
        # The result is the maximum time any ant takes to fall
        return max(max_left, max_right)