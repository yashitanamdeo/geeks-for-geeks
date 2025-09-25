# Problem Statement: https://www.geeksforgeeks.org/problems/generate-binary-numbers-1587115620/1

from collections import deque
class Solution:
    def generateBinary(self, n):
        ans=[]
        q=deque(["1"])
        for _ in range(n):
            s=q.popleft()
            ans.append(s)
            q.append(s+"0")
            q.append(s+"1")
        return ans