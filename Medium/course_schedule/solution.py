# Problem Statement: https://www.geeksforgeeks.org/problems/course-schedule/1

# User function Template for python3

import sys
from collections import defaultdict, deque


class Solution:
    def findOrder(self, n, m, prerequisites):
        graph = defaultdict(list)
        degree = [0]*n
        for c, p in prerequisites:
            graph[p].append(c)
            degree[c] += 1

        queue = deque([i for i in range(n) if degree[i] == 0])

        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)

            for x in graph[node]:
                degree[x] -= 1
                if degree[x] == 0:
                    queue.append(x)

        return ans if len(ans) == n else []


# {
 # Driver Code Starts
# Driver Program

sys.setrecursionlimit(10**6)


def check(graph, N, res):
    map = [0]*N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []

        for i in range(m):
            u, v = map(int, input().split())
            adj[v].append(u)
            prerequisites.append([u, v])

        ob = Solution()

        res = ob.findOrder(n, m, prerequisites)

        if (not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends
