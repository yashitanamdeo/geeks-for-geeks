# Problem Statement: https://practice.geeksforgeeks.org/problems/38f100615d0b2efa755e7b07f905e0f8cd2fe5df/1

#User function Template for python3

class Solution:
    def appleSequences(self, n, m, arr):
        # code here
        right, left = 0, 0
        ans = 0
        while right < n:
            if arr[right] == 'A':
                right += 1
            elif m > 0:
                right += 1
                m -= 1
            else:
                ans = max(ans, right-left)
                while arr[left] != 'O':
                    left += 1
                left += 1
                m += 1
        ans = max(ans, right-left)
        return ans


#{
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        temp = input().split()
        N = int(temp[0])
        M = int(temp[1])
        arr = input()

        ob = Solution()
        print(ob.appleSequences(N, M, arr))

# } Driver Code Ends
