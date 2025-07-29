# Problem Statement: https://www.geeksforgeeks.org/problems/mobile-numeric-keypad5456/1

#User function Template for python3
class Solution:
    def getCount(self, n):
        # Define the keypad layout
        keypad = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['-1', '0', '-1']
        ]
        
        def dfs(i, j, steps):
            if steps == 1:
                return 1
            
            if dp[int(keypad[i][j])][steps] != -1:
                return dp[int(keypad[i][j])][steps]
            
            # Count the same key press
            count = dfs(i, j, steps - 1)
            
            # Check up
            if i - 1 >= 0 and keypad[i - 1][j] != '-1':
                count += dfs(i - 1, j, steps - 1)
            # Check down
            if i + 1 <= 3 and keypad[i + 1][j] != '-1':
                count += dfs(i + 1, j, steps - 1)
            # Check left
            if j - 1 >= 0 and keypad[i][j - 1] != '-1':
                count += dfs(i, j - 1, steps - 1)
            # Check right
            if j + 1 <= 2 and keypad[i][j + 1] != '-1':
                count += dfs(i, j + 1, steps - 1)
            
            dp[int(keypad[i][j])][steps] = count
            return count
        
        # Initialize DP table
        dp = [[-1] * (n + 1) for _ in range(10)]
        result = 0
        
        for i in range(4):
            for j in range(3):
                if keypad[i][j] != '-1':
                    result += dfs(i, j, n)
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.getCount(n)
        print(ans)

# } Driver Code Ends