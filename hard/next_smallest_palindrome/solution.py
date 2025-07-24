# Problem Statement: https://practice.geeksforgeeks.org/problems/next-smallest-palindrome4740/1

#User function Template for python3
class Solution:

	def generateNextPalindrome(self,num, n ) :

        def isAll9():
            for i in num:
                if i != 9:
                    return False
            return True

        def gt(arr1, arr2):
            s1, s2 = '', ''
            for i in arr1:
                s1 += str(i)
            for i in arr2:
                s2 += str(i)
            return s1 > s2

        if isAll9():
            ans = [0] * (n+1)
            ans[0] = ans[-1] = 1
            return ans


        pal = [*num]
        pal[(n+1)//2:] = (pal[:n//2])[::-1]
        if gt(pal, num):
            return pal

        for left in range((n-1)//2, -1, -1):
            if num[left] < 9:
                num[left] += 1
                break
            num[left] = 0

        num[(n+1)//2:] = (num[:n//2])[::-1]
        return num



#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        num=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.generateNextPalindrome(num, n)
        for x in ans:
            print(x, end=" ")
        print()
        tc=tc-1
# } Driver Code Ends