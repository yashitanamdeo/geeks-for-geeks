# Problem Statement: https://www.geeksforgeeks.org/problems/shortest-prime-path--141631/1

# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3
from collections import deque

primes = [1]*10000
p = 2
while p*p < 10000:
    if primes[p] == 1:
        for i in range(p*p, 10000, p):
            primes[i] = 0
    p += 1


class Solution:
    def solve(self, num1, num2):
        visited = set()
        q = deque()
        q.append(num1)
        visited.add(num1)
        level = 0
        while q:
            n = len(q)
            for _ in range(n):
                num = q.popleft()
                if num == num2:
                    return level
                for i in range(4):
                    for j in range(0, 10):
                        if not (i == 0 and j == 0):
                            next = str(num)
                            next = next[:i]+str(j)+next[i+1:]
                            next = int(next)
                            if primes[next] and (next not in visited):
                                q.append(next)
                                visited.add(next)
            level += 1


# {
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        num1, num2 = map(int, input().split())
        ob = Solution()
        print(ob.solve(num1, num2))
# } Driver Code Ends
