# Problem Statement: https://practice.geeksforgeeks.org/problems/multiply-two-strings/1

# User function Template for python3

class Solution:
    def multiplyStrings(self, s1, s2):
        # Check if either of the strings is negative
        is_negative = (s1[0] == '-') ^ (s2[0] == '-')

        # Remove negative sign for conversion
        s1 = s1.lstrip('-')
        s2 = s2.lstrip('-')

        # Convert the strings to lists of integers
        num1 = [int(ch) for ch in s1][::-1]
        num2 = [int(ch) for ch in s2][::-1]

        # Initialize a result array with zeros
        result = [0] * (len(num1) + len(num2))

        # Perform multiplication
        for i in range(len(num1)):
            carry = 0
            for j in range(len(num2)):
                product = num1[i] * num2[j] + carry + result[i + j]
                carry = product // 10
                result[i + j] = product % 10
            result[i + len(num2)] += carry

        # Convert the result array to a string
        result_str = ''.join(map(str, result[::-1]))

        # Remove leading zeros
        result_str = result_str.lstrip('0')

        # Add negative sign if needed
        if is_negative and result_str != '0':
            result_str = '-' + result_str

        return result_str if result_str else '0'


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b = input().split()
        print(Solution().multiplyStrings(a.strip(), b.strip()))

# } Driver Code Ends
