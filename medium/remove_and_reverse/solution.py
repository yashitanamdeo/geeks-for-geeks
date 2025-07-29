# Problem Statement: https://practice.geeksforgeeks.org/problems/1e2f365be6114b671b915e145ec7dbcfdc432910/1

# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3
class Solution:
    def removeReverse(self, S):
        # code here
        dic = {}
        n = len(S)

        for i in S:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        start = 0
        stop = n-1
        rev = False
        st1 = ""
        st2 = ""
        while start <= stop:
            if rev == False:
                if dic[S[start]] == 1:
                    st1 += S[start]
                    start += 1

                else:
                    dic[S[start]] -= 1
                    st1 += "@"
                    start += 1
                    rev = True
            else:
                if dic[S[stop]] == 1:
                    st2 = S[stop]+st2
                    stop -= 1

                else:
                    dic[S[stop]] -= 1
                    st2 = "@"+st2
                    stop -= 1
                    rev = False
        st1 = st1+st2

        if rev == True:
            st1 = reversed(st1)
        ans = ""
        for i in st1:
            if i != '@':
                ans = ans+i
        return ans


# {
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.removeReverse(S)
        print(ans)


# } Driver Code Ends
