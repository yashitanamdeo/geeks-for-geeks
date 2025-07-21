# Problem Statement: https://www.geeksforgeeks.org/problems/divisor-game-1664432414/1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def divisorGame(self, n):
        if(n%2 == 0):
            return True
        return False
        
        

#{ 
 # Driver Code Starts.


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())

        obj = Solution()
        ans = obj.divisorGame(n)

        if ans:
            print("True")
        else:
            print("False")

        t -= 1
# } Driver Code Ends