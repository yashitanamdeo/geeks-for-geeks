# Problem Statement: https://practice.geeksforgeeks.org/problems/steps-by-knight5927/1#

class cell:
    
    def __init__(self, x = 0, y = 0, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist
        
class Solution():        
    # checks whether given position is 
    # inside the board
    def isInside(self, x, y, N):
        if (x >= 1 and x <= N and y >= 1 and y <= N): 
            return True
        return False
        
    # Method returns minimum step to reach
    # target position 
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        
        # all possible movments for the knight
        dx = [2, 2, -2, -2, 1, 1, -1, -1]
        dy = [1, -1, 1, -1, 2, -2, 2, -2]
        
        queue = []
        
        # push starting position of knight
        # with 0 distance
        queue.append(cell(KnightPos[0], KnightPos[1], 0))
        
        # make all cell unvisited 
        visited = [[False for i in range(N + 1)] for j in range(N + 1)]
        
        # visit starting state
        visited[KnightPos[0]][KnightPos[1]] = True
        
        # loop until we have one element in queue 
        while(len(queue) > 0):
            
            front = queue[0]
            queue.pop(0)
            
            # if current cell is equal to target 
            # cell, return its distance 
            if(front.x == TargetPos[0] and front.y == TargetPos[1]):
                return front.dist
                
            # iterate for all reachable states 
            for i in range(8):
                
                x = front.x + dx[i]
                y = front.y + dy[i]
                
                if(self.isInside(x, y, N) and not visited[x][y]):
                    visited[x][y] = True
                    queue.append(cell(x, y, front.dist + 1))
 	

#{ 
#  Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		KnightPos = list(map(int, input().split()))
		TargetPos = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
		print(ans)

# } Driver Code Ends