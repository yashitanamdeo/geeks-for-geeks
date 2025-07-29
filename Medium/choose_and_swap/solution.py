# Problem Statement: https://practice.geeksforgeeks.org/problems/choose-and-swap0531/1#

#User function Template for python3


#Find the first case where a element on the left is greater than element on the right. Swap!
class Solution:
    def chooseandswap (self, a):
       # code here
        s = list(set(a))
        s.sort()
        for smallestchar in s:
            smallestpos = a.index(smallestchar)
            found=False
            for ch in a:
                if ch > smallestchar:
                    found = True
                    break
            if not found:
                continue
            biggerpos = a.index(ch)
           
            if biggerpos<smallestpos:
                a = a.replace(ch,'#')
                a = a.replace(smallestchar,ch)
                a = a.replace('#',smallestchar)
                return a
           
        return a




#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        A = input()
        ans = ob.chooseandswap(A)
        print(ans)


# } Driver Code Ends