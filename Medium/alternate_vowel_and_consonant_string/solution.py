# Problem Statement: https://practice.geeksforgeeks.org/problems/alternate-vowel-and-consonant-string2939/1

#User function Template for python3

class Solution:
    def rearrange(self, S, N):
        # code here
        if N == 1:
            return S
        chars = [0] * 26
        for ch in S:
            chars[ord(ch) - 97] += 1
        vowels = sum([chars[0], chars[4], chars[8], chars[14], chars[20]])
        if abs(2 * vowels - sum(chars)) > 1:
            return -1
        vowels_string = ""
        consonent_string = ""
        for i in range(26):
            if i in [0, 4, 8, 14, 20]:
                vowels_string += chr(97+i) * chars[i]
            else:
                consonent_string += chr(97+i) * chars[i]
        
        if (vowels_string[0] < consonent_string[0]) and (len(vowels_string) >= len(consonent_string)):
            str1 = vowels_string
            str2 = consonent_string
        else:
            str2 = vowels_string
            str1 = consonent_string
        res = ""
        for i in range(len(str2)):
            res += str1[i] + str2[i]
        if i < len(str1)-1:
            res += str1[-1]
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N = int(input().strip())
        S = input().strip()
        ob=Solution()
        ans=ob.rearrange(S, N)
        print(ans)
# } Driver Code Ends