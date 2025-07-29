# Problem Statement: https://practice.geeksforgeeks.org/problems/next-happy-number4538/1

#User function Template for python3


class Solution:
    def isHappy(self,N):
        output_history = set()        #Saves the history of values that came from step 1
        while N not in output_history:        #Makes sure we don't run into an infinite loop (the value of N does not start to repeat)
            output_history.add(N)
            sq_digits = [int(i)**2 for i in str(N)]
            N = sum(sq_digits)
            if N==1:
                return True
        return False
    
    def nextHappy (self, N):
        while True:
            N += 1
            if self.isHappy(N):
                return N

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.nextHappy(N))
# } Driver Code Ends
