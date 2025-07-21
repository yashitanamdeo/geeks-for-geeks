# Problem Statement: https://www.geeksforgeeks.org/problems/additive-sequence/1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# return 1 in case of True and 0 in case of False
class Solution:
    def isAdditiveSequence(self, n: str) -> bool:
        if len(n) < 3:
            return 0
        
        def is_valid_number(s):
            return len(s) == 1 or s[0] != '0'
        
        for i in range(1, len(n) - 1):
            if not is_valid_number(n[:i]):
                continue
            for j in range(i + 1, len(n)):
                if not is_valid_number(n[i:j]):
                    continue
                num1 = int(n[:i])
                num2 = int(n[i:j])
                k = j
                while k < len(n):
                    num3 = num1 + num2
                    num3_str = str(num3)
                    if not n.startswith(num3_str, k):
                        break
                    k += len(num3_str)
                    num1, num2 = num2, num3
                    if k == len(n):
                        return 1
        return 0
        

#{ 
 # Driver Code Starts.
        
if __name__ == "__main__":
    sol = Solution()
    t = int(input())
    for _ in range(t):
        s = input()
        print(sol.isAdditiveSequence(s))

# } Driver Code Ends