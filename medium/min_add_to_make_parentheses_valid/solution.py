# Problem Statement: https://www.geeksforgeeks.org/problems/min-add-to-make-parentheses-valid/1

class Solution:
    def minParentheses(self, s):
        stack=[]
        ans=0
        for e in s:
            if e=="(":
                stack.append(e)
            else:
                if stack:
                    stack.pop()
                else:
                    ans+=1
        ans+=len(stack)
        return ans