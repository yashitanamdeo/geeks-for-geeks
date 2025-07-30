# Problem Statement: https://www.geeksforgeeks.org/problems/euler-circuit-and-path/1

class Solution:
    def isEulerCircuitExist(self, num_vertices, adjacency_list):
        # Count the degree of each vertex
        vertex_degrees = [0] * num_vertices
        for neighbors in adjacency_list:
            for neighbor in neighbors:
                vertex_degrees[neighbor] += 1

        # Count the number of vertices with odd degree
        odd_degree_count = sum(
            1 for degree in vertex_degrees if degree % 2 == 1)

        # Determine if an Euler circuit exists based on odd degree count
        if odd_degree_count == 0:
            # Euler circuit exists when all degrees are even
            return 2
        elif odd_degree_count <= 2:
            # Euler circuit exists when there are 0 or 2 vertices with odd degree
            return 1
        else:
            # No Euler circuit exists when more than 2 vertices have odd degree
            return 0


# {
 # Driver Code Starts


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isEulerCircuitExist(V, adj)
        print(ans)
# } Driver Code Ends
