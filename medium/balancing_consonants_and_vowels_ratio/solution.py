# Problem Statement: https://www.geeksforgeeks.org/problems/balancing-consonants-and-vowels-ratio/1

class Solution:
    def countBalanced(self, arr):
        from collections import defaultdict
        VOWELS = set("aeiou")
        prefix_balances = defaultdict(int, {0: 1})
        curr_balance = count = 0
        for word in arr:
            curr_balance += len(word) - 2 * sum(c in VOWELS for c in word)
            count += prefix_balances[curr_balance]
            prefix_balances[curr_balance] += 1
        return count