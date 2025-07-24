# Problem Statement: https://www.geeksforgeeks.org/problems/anagram-1587115620/1

#User function Template for python3


from collections import Counter
class Solution:
    def areAnagrams(self, s1, s2):
        return Counter(s1)==Counter(s2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends