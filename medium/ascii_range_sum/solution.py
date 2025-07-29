# Problem Statement: https://www.geeksforgeeks.org/problems/ascii-range-sum/1

class Solution:
    def asciirange(self, s):
        ans=[]
        for c in set(s):
            if s.find(c)!=s.rfind(c):
                a=0
                for i in range (s.find(c)+1,s.rfind(c)):
                   a+=ord(s[i])
                if a!=0:
                    ans.append(a)
        return ans