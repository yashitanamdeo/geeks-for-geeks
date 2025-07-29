# Problem Statement: https://practice.geeksforgeeks.org/problems/5be83263c7f2cb866c60b23b73bb38f88de2461c/1

#{
# Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def prefixSuffixString(self, s1, s2) -> int:
        #code here
        ans = 0
        i = 0
        j = 0
        m = len(s1)
        n = len(s2)
        while(i < m and j < n):
            if s2[j] in s1[i]:
                l = len(s2[j])
                if s2[j] == s1[i][:l] or s2[j] == s1[i][-l:]:
                    ans += 1
                    i = 0
                    j += 1
                else:
                    i += 1
            else:
                i += 1
        return ans

#{
 # Driver Code Starts.


if __name__ == "__main__":
    for _ in range(int(input())):
        s1 = list(map(str, input().split()))
        s2 = list(map(str, input().split()))
        obj = Solution()
        print(obj.prefixSuffixString(s1, s2))
# } Driver Code Ends
