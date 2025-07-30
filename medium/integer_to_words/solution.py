# Problem Statement: https://practice.geeksforgeeks.org/problems/number-to-words0335/1#

#User function Template for python3

class Solution:
    def convertToWords(self, n):
        # code here
        
        one = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", 
        "eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ",
        "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
        
        ten = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
        
        def numToWords(n,s):
            
            str = ""
            
            if n > 19:
                str += ten[(n // 10)] + one[(n % 10)]
            else:
                str += one[n]
                
            if n:
                str += s
                
            return str
        
        output = ""
        
        output += numToWords((n // 10000000), "crore ")
        output += numToWords(((n // 100000) % 100), "lakh ")
        output += numToWords(((n // 1000) % 100), "thousand ")
        output += numToWords(((n // 100) % 10), "hundred ")
        
        if(n > 100 and n % 100):
            output += "and "
            
        output += numToWords((n % 100), "")
        
        return output

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.convertToWords(n)
        print(ans)
        tc -= 1

# } Driver Code Ends