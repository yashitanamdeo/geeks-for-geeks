# Problem Statement: https://practice.geeksforgeeks.org/problems/alex-travelling/1

#User function Template for python3
import collections
from typing import List


class Solution:
    def minimumCost(self, flights: List[List[int]], n: int, k: int) -> int:
        # code here

        ## step-1
        adj_list = collections.defaultdict(list)
        for u, v, w in flights:
            adj_list[u].append((v, w))

         ## step-2
        dist = [-1 for _ in range(n+1)]
        q = collections.deque()
        dist[k] = 0
        q.append((k, dist[k]))
        ans = -1

       ##step-3
        while q:
            curr = q.popleft()
            node = curr[0]
            cost = curr[1]

            for neighbour in adj_list[node]:
                new_node = neighbour[0]
                new_cost = neighbour[1]
                if dist[new_node] == -1:
                    dist[new_node] = cost + new_cost
                    q.append((new_node, dist[new_node]))
                elif dist[new_node] > cost+new_cost:
                    dist[new_node] = cost + new_cost
                    q.append((new_node, dist[new_node]))

       #step-4
        for d in range(1, len(dist)):
            if dist[d] != -1:
                ans = max(ans, dist[d])
            else:
                return -1
        return ans

# Step1 : We create a adj_list and store the path with thier respective cost.

# I'm using python so i have used a dictionary

# step2: Create a distance-cost array and store the default distance_cost as -1 for n+1 elements since the given input's are 1-based indexing.

# make the k'th city 0 as it is the starting point.

# ALso create a queue and and append k as well as its cost

# step-3: Apply bfs.. the only catch here is that we ahve to make sure that the distance_cost is minimum for each node

# step-4: The minumum amount of money required to visit any city from k'th city will be the amount required to travel to the city which has the maximum price. ( hope this is clear if not : read it again )

# So, we make sure of that and return the ans

# ALso if we find the the distance_cost is -1, it implies that there is no path to that city from k'th city, hence we return -1


#{
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    T = int(input())
    for t in range(T):

        n = int(input())
        k = int(input())
        m = int(input())
        flights = []
        for i in range(m):
            u, v, wt = map(int, input().strip().split())
            flights.append([u, v, wt])
        obj = Solution()
        ans = obj.minimumCost(flights, n, k)
        print(ans)


# } Driver Code Ends
