# Problem Statement: https://www.geeksforgeeks.org/problems/nine-divisors3751/1

class Solution:
    def countNumbers(self, n: int) -> int:
        # Generate primes up to sqrt(n)
        limit = int(math.isqrt(n)) + 1
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        primes = []

        for i in range(2, limit + 1):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False

        count = 0

        # Case 1: p^8
        for p in primes:
            val = p ** 8
            if val <= n:
                count += 1
            else:
                break

        # Case 2: p^2 * q^2 for distinct primes p < q
        plen = len(primes)
        for i in range(plen):
            p2 = primes[i] ** 2
            if p2 * p2 > n:  # Early stop for outer loop
                break
            for j in range(i + 1, plen):
                q2 = primes[j] ** 2
                val = p2 * q2
                if val <= n:
                    count += 1
                else:
                    break

        return count