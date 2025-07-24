# Problem Statement: https://www.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1

#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends
#User function Template for python3

class Solution:
    def findSmallestMaxDist(self, stations, K):
        # Code here
        start, end = 0, stations[-1] - stations[0]
        while end - start > 1e-5:
            mid = (start + end)/2   # our guess (max distance)
            if self.isPossible(stations, K, mid):
                end = mid
            else:
                start = mid
        return end
    
    
    def isPossible(self, stations, k, maxDist):
        stationsToAdd = 0
        for i in range(1, len(stations)):
            stationsToAdd += (stations[i] - stations[i-1])//maxDist
        return stationsToAdd <= k
        

#{ 
 # Driver Code Starts.
import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        stations = list(map(int, input().split()))
        K = int(input())
        ob = Solution()
        print('%.2f' % ob.findSmallestMaxDist(stations, K))
# } Driver Code Ends