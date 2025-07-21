# Problem Statement: https://practice.geeksforgeeks.org/problems/counts-zeros-xor-pairs0349/1

#User function Template for python3


from collections import Counter
def calculate (arr, n) : 
    Result = 0
    Count = Counter(arr)
    for K,V in Count.items():
        if(V >= 2):
            Result += (V*(V-1))//2
    return Result



#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = calculate(arr, n)
    print(res)


# } Driver Code Ends