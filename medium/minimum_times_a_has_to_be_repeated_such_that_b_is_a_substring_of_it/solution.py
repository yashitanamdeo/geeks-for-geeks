# Problem Statement: https://practice.geeksforgeeks.org/problems/fda70097eb2895ecfff269849b6a8aace441947c/1

#User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        # code here
        a = set(A)
        b = set(B)
        if b.issubset(a):
            S = ""
            ans = 0
            while len(S) < len(B):
                S += A
                ans += 1
            if B in S:
                return ans
            elif B in S+A:
                return ans + 1
            else:
                return -1
        else:
            return -1


class Solution2:
    def minRepeats(self, A, B):
        # code here 
        dummy = A
        for i in range(1,10**3): #acc. to constraints it cannot repeat more than 10**3 times
            if B in dummy:
                return i
            dummy += A
        return -1
        '''
        check if B is present in A - if it is then return the number of times
        loop ran in order to return minimum number of repetitions of string A 
        else if it doesn't return therefore B cannot be a substring of A in any case so return -1
        '''

#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = input()
        B = input()

        ob = Solution()
        print(ob.minRepeats(A, B))
# } Driver Code Ends
