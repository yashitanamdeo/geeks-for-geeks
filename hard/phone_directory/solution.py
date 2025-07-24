# Problem Statement: https://practice.geeksforgeeks.org/problems/phone-directory4628/1

# User function Template for python3

from collections import defaultdict


class Solution:

    def displayContacts(self, n, contact, s):
        # code here
        m = defaultdict(set)
        contact.sort()
        for i in contact:
            for j in range(1, len(i)+1):
                m[i[:j]].add(i)
        res = []

        for i in range(1, len(s)+1):
            if s[:i] in m:
                res.append(sorted(m[s[:i]]))
            else:
                res.append([0])
        return (res)


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        contact = input().split()
        s = input()

        ob = Solution()
        ans = ob.displayContacts(n, contact, s)
        for i in range(len(s)):
            for val in ans[i]:
                print(val, end=" ")
            print()
# } Driver Code Ends
