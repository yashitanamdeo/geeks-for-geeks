# Problem Statement: https://practice.geeksforgeeks.org/problems/sort-by-set-bit-count1153/1

#User function Template for python3
from collections import defaultdict 

class Solution:
    def sortBySetBitCount(self, arr, n):
        mp=defaultdict(list)
        for i in arr:
            n=bin(i).replace('0b',"")
            mp[n.count('1')].append(i)
        l=[]
        for i in mp.values():
            for j in i[::-1]:
                l.append(j)
        l=l[::-1]
        arr[:]=l[:]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortBySetBitCount(arr, n)
        print(*arr)

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends