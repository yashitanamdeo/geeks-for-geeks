# Problem Statement: https://www.geeksforgeeks.org/problems/assign-mice-holes3053/1

class Solution:
    def assignHole(self, mices, holes):
        # code here
        mices.sort()
        holes.sort()
        max_time = 0

        l = len(mices)
        i = 0
        while i<l :
            diff = abs(mices[i] - holes[i])
            max_time = max(max_time, diff)
            i += 1
         
        return max_time
