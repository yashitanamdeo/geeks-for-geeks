# Problem Statement: https://www.geeksforgeeks.org/problems/insert-interval-1666733333/1

class Solution:
    def insertInterval(self, intervals, newInterval):
        result = []
        n = len(intervals)
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result