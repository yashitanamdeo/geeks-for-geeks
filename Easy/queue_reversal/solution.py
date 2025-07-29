# Problem Statement: https://practice.geeksforgeeks.org/problems/queue-reversal/1

#User function Template for python3

class Solution:
    #Function to reverse the queue.
    def rev(self, q):
        n=q.maxsize
        l=[]
        for i in range(n):
            l.append(q.get())
        for i in range(n):
            q.put(l.pop())
        return q


#{ 
 # Driver Code Starts

#Initial Template for Python 3

from queue import Queue
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        q=Queue(maxsize=n)
        for j in a:
            q.put(j)
            
        ob = Solution()
        q=ob.rev(q)
        for i in ran
        ge(0,n):
            print(q.get(),end=" ")
        print()
# } Driver Code Ends