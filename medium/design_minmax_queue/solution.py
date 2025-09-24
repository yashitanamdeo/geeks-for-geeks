# Problem Statement: https://www.geeksforgeeks.org/problems/design-minmax-queue/1

from collections import deque
class SpecialQueue:
    def __init__(self):
        self.queue=deque()
        self.minDeque=deque()
        self.maxDeque=deque()

    def enqueue(self, x):
        self.queue.append(x)
        while self.minDeque and self.minDeque[-1]>x:
            self.minDeque.pop()
        self.minDeque.append(x)
        while self.maxDeque and self.maxDeque[-1]<x:
            self.maxDeque.pop()
        self.maxDeque.append(x)

    def dequeue(self):
        if not self.queue:
            return -1
        val=self.queue.popleft()
        if val==self.minDeque[0]:
            self.minDeque.popleft()
        if val==self.maxDeque[0]:
            self.maxDeque.popleft()
    
    def getFront(self):
        if self.queue:
            return self.queue[0]
        return -1
    
    def getMin(self):
        if self.minDeque:
            return self.minDeque[0]
        return -1

    def getMax(self):
        if self.maxDeque:
            return self.maxDeque[0]
        return -1
