# Problem Statement: https://www.geeksforgeeks.org/problems/string-palindromic-ignoring-spaces4723/1

class Solution:
    def isPalinSent(self, s: str) -> bool:
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        return cleaned == cleaned[::-1]