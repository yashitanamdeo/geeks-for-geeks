# Problem Statement: https://www.geeksforgeeks.org/problems/count-of-strings-that-can-be-formed-using-a-b-and-c-under-given-constraints1135/1

# User function Template for python3

class Solution:

    def countStr(self, length):
        # Case 1: Strings with all 'a'
        strings_all_a = 1

        # Case 2: Strings with at most 1 'b'
        strings_at_most_1_b = length

        # Case 3: Strings with at most 1 'c'
        strings_at_most_1_c = length

        # Case 4: Strings with one 'b' and one 'c'
        strings_one_b_one_c = length * (length - 1)

        # Case 5: Strings with two 'c'
        strings_two_c = (length * (length - 1)) // 2

        # Case 6: Strings with one 'b' and two 'c'
        strings_one_b_two_c = (length * (length - 1) * (length - 2)) // 2

        total_strings = strings_all_a + strings_at_most_1_b + strings_at_most_1_c + \
            strings_one_b_one_c + strings_two_c + strings_one_b_two_c

        return total_strings


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countStr(n))
# } Driver Code Ends
