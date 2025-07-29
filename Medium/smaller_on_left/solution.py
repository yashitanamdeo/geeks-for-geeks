# Problem Statement: https://practice.geeksforgeeks.org/problems/smaller-on-left20360700/1#

#User function Template for python3
import bisect

def Smallestonleft (arr,  n) : 
    #Complete the function
    stack = []
    answer = []
    answer.append(-1)
    stack.append(arr[0])
    for i in range(1,n):
        bisect.insort(stack,arr[i])
        it = bisect.bisect_left(stack,arr[i])

        if (it):

            answer.append(stack[it-1])
        else:
            answer.append(-1)
    return answer

#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = Smallestonleft(arr, n);
    for each in res:
        print(each,end=' ')
    print()




# } Driver Code Ends