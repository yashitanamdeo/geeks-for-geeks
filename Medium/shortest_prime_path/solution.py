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


class Solution2:
    def __init__(self):
        # Every index of prime stores zero or one
        # If prime[i] is zero means i is not a prime
        # If prime[i] is one means i is a prime
        self.prime=[1 for i in range(10001)]

    def shortestPath(self,num1, num2):
        prime = [1 for i in range(10000)]
        for p in range(2, int(9999 ** 0.5) + 1):
            if prime[p]:
                for i in range(p * p, 10000, p):
                    prime[i] = 0
        q = [(num1, 0)]
        st = {num1}
        while q:
            x, y = q.pop(0)
            if x == num2:
                return y
            for k in range(1, 5):
                for a in range(10):
                    j = 10 ** (4 - k)
                    l = (x // j) % 10
                    if l != a:
                        newl = x + (a - l) * j
                        if newl not in st and prime[newl] and 1000 <= newl < 10000:
                            q.append((newl, y + 1))
                            st.add(newl)
        return -1


# {
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        num1, num2 = map(int, input().split())
        ob = Solution()
        print(ob.solve(num1, num2))
# } Driver Code Ends
