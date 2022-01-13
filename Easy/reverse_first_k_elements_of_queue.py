# Problem Statement: https://practice.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1#

#User function Template for python3
'''
Function Arguments :
		@param  : q ( given queue to be used), k(Integer )
		@return : list, just reverse the first k elements of queue and return new queue
'''

#Function to reverse first k elements of a queue.
def modifyQueue(q,k):
    # code here
    a = q[:k]
    b = q[k:]
    a = a[::-1]
    return (a+b)
    #return q[:k][::-1] + q[k:]

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))

        queue = [] # our queue to be used
        for i in range(n):
            queue.append(a[i]) # enqueue elements of array in our queue

        print(*modifyQueue(queue,k))
# } Driver Code Ends