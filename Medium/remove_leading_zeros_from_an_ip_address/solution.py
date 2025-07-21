# Problem Statement: https://practice.geeksforgeeks.org/problems/remove-leading-zeros-from-an-ip-address3530/1

#User function Template for python3

class Solution:
    def newIPAdd(self, S):
        new_ip = ''
        for ch in S.split('.'):
            flag = 0
            for c in ch:
                if c == '0' and flag == 0:
                    continue
                else:
                    flag = 1
                    new_ip += c
            if flag == 0: new_ip += '0'
            new_ip += "."
        return new_ip[:-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.newIPAdd(s)
        print(ans)
# } Driver Code Ends