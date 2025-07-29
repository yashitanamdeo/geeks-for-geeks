# Problem Statement: https://practice.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1

#User function Template for python3

from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        if start == end:
            return 0
        from collections import deque
        MODULO = 10**5
        visited = [False] * MODULO
        q = deque([(start, 0)])
        while q:
            k, steps = q.popleft()
            for a in arr:
                l = (k * a) % MODULO
                if visited[l]:
                    continue
                if l == end:
                    return steps + 1
                visited[l] = True
                q.append((l, steps + 1))
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends