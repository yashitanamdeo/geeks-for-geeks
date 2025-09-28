# Problem Statement: https://www.geeksforgeeks.org/problems/longest-bounded-difference-subarray/1

from collections import deque
class Solution:
    def longestSubarray(self, arr, x):
        n=len(arr)
        maxQ,minQ=deque(),deque()
        length=0
        start=0
        l=0
        for r in range(n):
            while maxQ and arr[maxQ[-1]]<arr[r]:
                maxQ.pop()
            maxQ.append(r)
            while minQ and arr[minQ[-1]]>arr[r]:
                minQ.pop()
            minQ.append(r)
            while arr[maxQ[0]]-arr[minQ[0]]>x:
                l+=1
                if maxQ[0]<l:
                    maxQ.popleft()
                if minQ[0]<l:
                    minQ.popleft()
            if r-l+1>length:
                length=r-l+1
                start=l
        return arr[start:start+length]