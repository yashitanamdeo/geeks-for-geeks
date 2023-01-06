class Solution:
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
