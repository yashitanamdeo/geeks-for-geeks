# Problem Statement: https://www.geeksforgeeks.org/problems/game-with-string4100/1

#User function Template for python3

from collections import defaultdict
class Solution:
    def minValue(self, s, k):
        # code here
        char_count=defaultdict(int)
        for char in s:
            char_count[char]+=1
        values=list(char_count.values())
        values.sort()
        while k!=0:
            values[-1]-=1
            k=k-1
            values.sort()
        sum=0
        for ele in values:
            sum+=ele**2
        return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends