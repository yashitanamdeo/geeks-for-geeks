# Problem Statement: https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1

class Solution:
    def minJumps(self, arr):
	    # each step to check how far jump can reached
	    
        # mock a virtual queue
        # visualize jump can happened in a segment [start, end]
        # if any jump happened in the segment can't jump outside the segment
        # then can't reach the end
        # next segment jump will be [prev-end+1, new-end-from-the-segment-jumps]
        
        start, end, jumps = 0, 0, 0 # first segment is (0, 0)
        while start <= end: #valid segment
            if end >= len(arr)-1:
                return jumps
            
            new_end = end
            for i in range(start, end+1): #traverse all possible jump to find the next best end
                new_end = max(new_end, arr[i]+i)
            
            start, end = end+1, new_end
            jumps += 1
        
        return -1