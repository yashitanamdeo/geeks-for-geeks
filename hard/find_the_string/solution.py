# Problem Statement: https://www.geeksforgeeks.org/problems/find-the-string/1

# User function Template for python3

import sys


class Solution:
    def __init__(self):
        self.result = None

    def generate_strings(self, length, base):
        """
        Generates all possible strings of given length using the characters from 0 to base-1.
        """
        def dfs(n, k, current_string, result_set):
            """
            Depth-first search to generate all possible strings of length n.
            """
            if n == 0:
                result_set.add(current_string)
                return result_set

            for i in range(k):
                result_set = dfs(n - 1, k, current_string + str(i), result_set)

            return result_set

        ans_set = set()
        ans_set = dfs(length, base, '', ans_set)
        return ans_set

    def build_graph(self, strings, base):
        """
        Builds a graph where two strings are connected if they have a common suffix and differ only in the last character.
        """
        graph = {}

        for i in strings:
            for z in range(base):
                neighbor = i[1:] + str(z)
                if neighbor in strings and neighbor != i:
                    if i in graph:
                        graph[i].append(neighbor)
                    else:
                        graph[i] = [neighbor]

        return graph

    def findString(self, N, K):
        """
        Finds the lexicographically smallest string such that each string of length N with characters from 0 to K-1
        is a suffix of the constructed string.
        """
        strings = self.generate_strings(N, K)
        graph = self.build_graph(strings, K)
        visited = set()

        def find(ele, current_string):
            """
            Recursive function to find the lexicographically smallest string.
            """
            visited.add(ele)

            if len(visited) == (K ** N):
                self.result = current_string
                return True

            for neighbor in graph[ele]:
                if neighbor not in visited and find(neighbor, current_string + neighbor[-1]):
                    return True

            visited.remove(ele)
            return False

        for i in strings:
            if find(i, i):
                return self.result

        return self.result


# {
 # Driver Code Starts
# Initial Template for Python 3

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, K = map(int, input().split())

        ob = Solution()
        ans = ob.findString(N, K)
        ok = 1
        for i in ans:
            if ord(i) < 48 or ord(i) > K-1+48:
                ok = 0
        if not ok:
            print(-1)
            continue
        d = dict()
        i = 0
        while i+N-1 < len(ans):
            d[ans[i:i+N]] = 1
            i += 1
        tot = pow(K, N)
        if len(d) == tot:
            print(len(ans))
        else:
            print(-1)
# } Driver Code Ends
