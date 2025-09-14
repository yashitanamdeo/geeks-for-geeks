# Problem Statement: https://www.geeksforgeeks.org/problems/circular-tour-1587115620/1

class Solution:
  
    def startStation(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        tank = 0
        for i in range (len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start

