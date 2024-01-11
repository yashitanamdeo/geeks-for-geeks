# Problem Statement: https://www.geeksforgeeks.org/problems/remove-k-digits/1

#User function Template for python3

class Solution:

    def removeKdigits(self, S, k):
        stack=[]
        for i in S:
            while stack and k>0 and i<stack[-1]:
                k-=1
                stack.pop()
            stack.append(i)
        while k>0:
            stack.pop()
            k-=1
        if len(stack)==stack.count('0'):
            return '0'                                                                                                                                                                                                                                                                                       
        for i in range(len(stack)):
            if stack[i]=='0':
                continue
            if stack[i]!='0':
                return "".join(stack[i:])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends
