# Problem Statement: https://www.geeksforgeeks.org/problems/number-following-a-pattern3126/1

#User function Template for python3
class Solution:
    def printMinNumberForPattern(self, pattern):
        result = []  # List to store the generated number
        stack = []   # Stack to keep track of increasing sequence
        num = 1      # Counter for increasing numbers

        for char in pattern:
            stack.append(str(num))
            num += 1

            if char == "I":
                # If 'I' is encountered, add the reversed stack to the result
                result += stack[::-1]
                stack = []

        # Add the remaining numbers to the result
        stack.append(str(num))
        result += stack[::-1]

        # Convert the list of digits to an integer and return
        return int(''.join(result))


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends