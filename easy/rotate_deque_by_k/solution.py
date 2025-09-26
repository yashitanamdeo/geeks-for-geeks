# Problem Statement: https://www.geeksforgeeks.org/problems/rotate-deque-by-k/1

class Solution:    
    def rotateDeque(self, dq, tp, k):
        #code here
        k=k%len(dq)
        if tp==1:
            while k:
                dq.appendleft(dq.pop())
                k-=1
        else:
            while k:
                dq.append(dq.popleft())
                k-=1
        return dq