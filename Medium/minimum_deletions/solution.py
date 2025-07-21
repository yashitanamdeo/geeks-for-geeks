# Problem Statement: https://practice.geeksforgeeks.org/problems/minimum-deletitions1648/1

#User function Template for python3

class Solution:
    def minimumNumberOfDeletions(self, input_string):
        # Get the length of the input string
        string_length = len(input_string)
        
        # Initialize a 2D array for dynamic programming
        dp = [[0] * string_length for _ in range(string_length)]
       
        # Initialize the base cases for substrings of length 1 (single characters)
        for i in range(string_length):
            dp[i][i] = 1
       
        # Fill the DP table for substrings of length 2 and above
        for substring_length in range(2, string_length + 1):
            for start_index in range(string_length - substring_length + 1):
                end_index = start_index + substring_length - 1
                
                # Check if the characters at both ends of the substring match
                if input_string[start_index] == input_string[end_index] and substring_length == 2:
                    # Special case: Substring of length 2 with matching characters
                    dp[start_index][end_index] = 2
                elif input_string[start_index] == input_string[end_index]:
                    # Characters match, so update the DP table using the result from a shorter substring
                    dp[start_index][end_index] = dp[start_index + 1][end_index - 1] + 2
                else:
                    # Characters don't match, so take the maximum from two possible options
                    dp[start_index][end_index] = max(dp[start_index][end_index - 1], dp[start_index + 1][end_index])
       
        # The minimum number of deletions required to form a palindrome is the complement of the longest palindromic subsequence
        return string_length - dp[0][string_length - 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends