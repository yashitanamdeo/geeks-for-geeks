# Problem Statement: https://practice.geeksforgeeks.org/problems/build-the-smallest2841/1

#User function Template for python3

class Solution:

    def buildLowestNumber(self, S,N):
        # code here
        stack = []
        
        for i in S:
            if len(stack) and stack[-1] > i:
                while N > 0 and len(stack) and stack[-1] > i:
                    stack.pop()
                    N -= 1
                stack.append(i)
            else:
                stack.append(i)
        while N > 0:
            stack.pop()
            N -= 1
        ans = ''.join(stack)
        result = ans.lstrip('0')
        if len(result) == 0:
            return "0"
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        S = input()

        solObj = Solution()

        print(solObj.buildLowestNumber(S,N))
# } Driver Code Ends