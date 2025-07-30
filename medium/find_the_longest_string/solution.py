# Problem Statement: https://practice.geeksforgeeks.org/problems/8d157f11af5416087251513cfc38ffc4d23be308/1

#User function Template for python3


class Solution():

    def longestString(self, arr, n):

        #your code goes here
        arr.sort()
        max=""
        dict={}
        dict[""]=1
        for i in range(n):
            if arr[i][:-1] in dict:
                dict[arr[i]]=1
                if len(max)<len(arr[i]):
                    max=arr[i]

        return max



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [i for i in input().split()]
        print(Solution().longestString(arr,n))
# } Driver Code Ends
