# Problem Statement: https://www.geeksforgeeks.org/problems/search-pattern0205/1

# User function Template for python3

class Solution:
    def search(self, pat, txt):
        if pat not in txt:
            return [-1]
        i = txt.find(pat)
        l = [i+1]
        while (i != -1):
            i = txt.find(pat, i+1)
            if (i != -1):
                l.append(i+1)

        return l


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print(-1, end="")
        for value in ans:
            print(value, end=' ')
        print()
# } Driver Code Ends
