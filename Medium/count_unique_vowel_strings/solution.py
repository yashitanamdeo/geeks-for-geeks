# Problem Statement: https://www.geeksforgeeks.org/problems/count-unique-vowel-strings/1

class Solution:
    def vowelCount(self, s):
        from functools import reduce
        key = {}
        vowels = 'aeiou'
        for i in s:
            if i in vowels:
                if i not in key:
                    key[i] = 1
                else:
                    key[i] += 1
        if len(key.keys()) == 0:
            return 0
        key_prod = reduce(lambda x,y: x*y, key.values())
        fact = reduce(lambda x,y: x*y, [i for i in range(1,len(key.keys())+1)])
        return fact * key_prod