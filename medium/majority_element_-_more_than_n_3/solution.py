# Problem Statement: https://www.geeksforgeeks.org/problems/majority-vote/1

class Solution:
    def findMajority(self, arr):
        # code here
        n = len(arr)
        one_third = n//3 # Calculated the value of floor of n/3
        cnt = 0
        arr.sort() #for better understanding and tallying the values
        freq = {}
        ans = []
        for i in arr:
            freq[i]=freq.get(i,0) +1 # Counted the frequency of the each element
        for key in freq:
            if freq[key] > one_third: # Condition of "< floor of n/3 applied here.
                ans.append(key) # Stored in separate array
    
        return ans #Returned the answer