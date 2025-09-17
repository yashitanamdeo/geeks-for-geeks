# Problem Statement: https://practice.geeksforgeeks.org/problems/decode-the-string2444/1

#User function Template for python3

class Solution:

    def decodedString(self, s):
        # code here
        charStack = []
        number = 0
        finalString = ''
        while s:
            st = ''
            if s[0] == '[':
                num = ''
                while charStack and charStack[-1].isdigit():
                    num = charStack.pop()+num
                number = int(num)
                s = s[1:]
                ans, s = self.decodedString(s)
                for i in range(number):
                    st += ans
                st1 = ''
                while charStack:
                    st1 = charStack.pop() + st1
                finalString += st1
                finalString += st
                s = s[1:]
            elif s[0] == ']':
                st1 = ''
                while charStack:
                    st1 = charStack.pop() + st1
                finalString = finalString+st1
                return [finalString, s]
            else:
                charStack.append(s[0])
                s = s[1:]
        return finalString


class Solution2:
    def decodedString(self, s):
        # code here
        stack = []
        for i in s:
            if i == ']':
                expand = ''
                while stack[-1] != '[':
                    expand = stack.pop() + expand
                stack.pop()

                mul = ''
                while stack and stack[-1].isdigit():
                    mul = stack.pop() + mul
                
                stack.append(int(mul) * expand)
                continue
            
            stack.append(i)
            
        return ''.join(stack)
#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends
