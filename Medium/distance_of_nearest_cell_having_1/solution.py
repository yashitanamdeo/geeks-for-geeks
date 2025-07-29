# Problem Statement: https://practice.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1

from collections import deque
from collections import namedtuple


class Solution:
    #Function to find distance of nearest 1 in the grid for each cell.
  def nearest(self, grid):
    rows = len(grid)
    cols = len(grid[0])

    # Default all nodes to as unreachable
    distance = [[float("inf") for _ in range(cols)] for _ in range(rows)]

    DistMetric = namedtuple("DistanceMetrics", "i j distance")
    nodes_to_explore = deque()

    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == 1:
          distance[i][j] = 0
          nodes_to_explore.append(DistMetric(i, j, 0))
    #               right    down      left     up
    displacements = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    while nodes_to_explore:
      dist = nodes_to_explore.popleft()
      # i, j, cur_dist = dist
      cur_i, cur_j, cur_dist = dist.i, dist.j, dist.distance

      for displacement in displacements:
        next_i, next_j = cur_i + displacement[0],  cur_j + displacement[1]
        # Add for exploration only if the i, j is valid and we can get a better distance
        if next_i >= 0 and next_i < rows and next_j >= 0 and next_j < cols:
          if distance[next_i][next_j] != 0 and distance[next_i][next_j] > cur_dist + 1:
            distance[next_i][next_j] = cur_dist + 1
            nodes_to_explore.append(DistMetric(next_i, next_j, cur_dist+1))

    return distance


#{
 # Driver Code Starts
if __name__ == '__main__':
	T = int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.nearest(grid)
		for i in ans:
			for j in i:
				print(j, end=" ")
			print()

# } Driver Code Ends
