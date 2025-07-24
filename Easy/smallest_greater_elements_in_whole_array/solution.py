# Problem Statement: https://practice.geeksforgeeks.org/problems/smallest-greater-elements-in-whole-array2751/1#

#User function Template for python3


def greaterElement (arr,  n) : 
   #Complete the function
    s = list(set(arr))
    s = sorted(s)
   
    temp_dict = {s[i]:i for i in range(len(s))}
   
    for i in range(n):
        ind = temp_dict[arr[i]]
       
        if ind + 1 == len(s):
            arr[i] =- 10000000
        else:
            arr[i] = s[ind+1]
    return arr


#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = greaterElement(arr, n);
    ans = ""
    for i in res:
        if(i == -10000000):
            ans += "_ "
        else:
            ans += str(i)+" "
    print(ans)



# } Driver Code Ends