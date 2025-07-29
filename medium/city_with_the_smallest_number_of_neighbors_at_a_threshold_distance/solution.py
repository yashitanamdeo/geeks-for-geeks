# Problem Statement: https://www.geeksforgeeks.org/problems/city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/1

#User function Template for python3

from typing import List
import heapq

class Solution:
    def findCity(self, n: int, m: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[] for _ in range(n)]
        for it in edges:
            adj[it[0]].append((it[1], it[2]))
            adj[it[1]].append((it[0], it[2]))

        city_no = -1
        min_city_count = float('inf')

        for i in range(n):
            dist = [float('inf')] * n
            pq = [(0, i)]
            dist[i] = 0

            while pq:
                distance, node = heapq.heappop(pq)
                for adj_node, adj_weight in adj[node]:
                    if distance + adj_weight < dist[adj_node]:
                        dist[adj_node] = distance + adj_weight
                        heapq.heappush(pq, (dist[adj_node], adj_node))

            count = sum(1 for j in range(n) if dist[j] <= distanceThreshold)
            if count <= min_city_count:
                min_city_count = count
                city_no = i

        return city_no

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        
        n, m = map(int, input().strip().split())
        edges = []
        for i in range(m):
            u, v, wt = map(int, input().strip().split())
            edges.append([u, v, wt])
        distanceThreshold = int(input())
        obj = Solution()
        ans = obj.findCity(n, m, edges, distanceThreshold)
        print(ans)
            

# } Driver Code Ends