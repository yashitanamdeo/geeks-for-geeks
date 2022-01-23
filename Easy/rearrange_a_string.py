#User function Template for python3

class Solution:
   def arrangeString(self, s):
  
        l1 = []
        l2 = []
       
        for i in range(0,len(s)):
            if (s[i]=="0")or(s[i]== '1')or(s[i]== '3')or(s[i]== '4')or(s[i]== '5')or(s[i]== '6')or(s[i]== '7')or(s[i]== '8')or(s[i]== '9')or(s[i]== '2'):
                l1.append(int(s[i]))
            else:
                l2.append(s[i])
        l1.sort()
        l2.sort()
       
        sum = 0
        res = ""
        for x in range(0,len(l1)):
            sum+= l1[x]
        for y in range(0,len(l2)):
            res += l2[y]
        return res+str(sum)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.arrangeString(s)
        print(ans)
# } Driver Code Ends