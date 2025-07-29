# Problem Statement: https://www.geeksforgeeks.org/problems/juggler-sequence3930/1

#User function Template for python3

class Solution:
        def jugglerSequence(self, n):
            # code here
            l=[]
            a=n
            while a!=1:
                l.append(a)
                if a%2:
                    a=int(a**(3/2))
                else:
                    a=int(a**(1/2))
            l.append(1)
                
            return l

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        arr = ob.jugglerSequence(n)
        for i in (arr):
            print(i, end=" ")
        print()

# } Driver Code Ends