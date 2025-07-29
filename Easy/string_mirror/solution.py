# Problem Statement: https://practice.geeksforgeeks.org/problems/d385b9d635b7b10eef6bf365b84922aaeec9eb98/1

class Solution:
    def stringMirror(self, s):
        res = tmp = s[0]

        for ch in s[1:]:
            if tmp < ch or ch == s[0]:
                break
            res += ch
            tmp = ch

        return res + res[::-1]


# {
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        str = (input())

        obj = Solution()
        res = obj.stringMirror(str)

        print(res)


# } Driver Code Ends
