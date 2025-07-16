# Problem Statement: https://www.geeksforgeeks.org/problems/power-of-k-in-n-where-k-may-be-non-prime4206/1

import math
class Solution:

    def isPrime(self, n: int) -> bool:
        """
        Checks if a number is prime.

        Args:
            n: The number to check.

        Returns:
            True if n is prime, False otherwise.
        """
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def factors(self, k: int) -> list[int]:
        """
        Finds the prime factors of a number.

        Args:
            k: The number to factorize.

        Returns:
            A list of prime factors of k.
        """
        factors_list = []
        for i in range(2, k + 1):
            if k % i == 0 and self.isPrime(i):
                factors_list.append(i)
        return factors_list

    def maxKPower(self, N: int, K: int) -> int:
        """
        Calculates the largest power of K that divides N!.

        Args:
            N: The upper limit of the factorial (N!).
            K: The number whose largest power needs to be found.

        Returns:
            The largest power of K that divides N!.
        """
        factors_of_k = self.factors(K)
        n = len(factors_of_k)
        count_of_factors = [0] * n

        # Count the number of occurrences of the prime factors in N!
        for i in range(n):
            factor = factors_of_k[i]
            count = 0
            for j in range(factor, N + 1, factor):
                num = j
                while num >= factor and num % factor == 0:
                    num //= factor
                    count += 1
            count_of_factors[i] = count

        # Determine the minimum frequency of prime factors required to form K
        min_count_req = [0] * n
        for i in range(n):
            factor = factors_of_k[i]
            count = 0
            num = K
            while num >= factor and num % factor == 0:
                num //= factor
                count += 1
            min_count_req[i] = count

        # Calculate the maximum number of times K occurs in N!
        ans = float('inf')
        for i in range(n):
            total_count = count_of_factors[i]
            required_count = min_count_req[i]
            ans = min(ans, total_count // required_count)

        return 0 if ans == float('inf') else ans