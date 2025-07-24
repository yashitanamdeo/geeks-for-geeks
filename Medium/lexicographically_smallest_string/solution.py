# Problem Statement: https://practice.geeksforgeeks.org/problems/mila-and-strings0435/1

# User function Template for python3
class Solution:

    def lexicographicallySmallest(self, S, k):
        ans = ""
        l = len(S)
        if (l & (l-1)):
            k += k
        else:
            k //= 2
        if k >= l:
            return "-1"
        st = []
        for i in range(l):
            while st and k > 0 and st[-1] > S[i]:
                st.pop()
                k -= 1
            st.append(S[i])
        if k > 0:
            while k > 0:
                st.pop()
                k -= 1
        while st:
            ans = st[-1]+ans
            st.pop()
        return ans


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, k = input().split()
        k = int(k)

        ob = Solution()
        print(ob.lexicographicallySmallest(S, k))
# } Driver Code Ends
