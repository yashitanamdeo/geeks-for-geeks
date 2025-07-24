# Problem Statement: https://practice.geeksforgeeks.org/problems/4dfa8ba14d4c94f4d7637b6b5246782412f3aeb8/1

#User function Template for python3


class Solution:
    def maxLength(self, arr, n):
        pos_len, neg_len, ans = 0, 0, 0
        for e in arr:
            if e == 0:
                pos_len = neg_len = 0
            elif e < 0:
                pos_len, neg_len = neg_len+1 if neg_len else 0, pos_len+1
            else:
                neg_len, pos_len = neg_len+1 if neg_len else 0, pos_len+1
            ans = max(ans, pos_len)
        return ans


#{
 # Driver Code Starts
#Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.maxLength(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
