# Problem Statement: https://practice.geeksforgeeks.org/problems/save-your-life4601/1

# User function Template for python3
import sys


class Solution:
    def maxSum(self, w, x, b, n):
        # code here

        changed_ascii = dict(zip(x, b))

        max_ending_here, max_so_far = 0, -1*sys.maxsize

        '''
            Using Kadane's algorithm along with that additional storage of indices is required to know the start and the end index
            
        '''

        pre_start_idx, post_start_idx, end_idx = 0, 0, 0  # initial values of indices
        # two start indices are given because start_index need to partial represent the both the previous max substring start index
        # and the current sequence start index

        for i in range(len(w)):

            if w[i] in changed_ascii:
                max_ending_here += changed_ascii[w[i]]
            else:
                max_ending_here += ord(w[i])

            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                # when the maximum is updated
                # Then updating the start with the current substring start index (longest ascii sum substring), end_index with the current index (because longest sum substring is changed)
                pre_start_idx, end_idx = post_start_idx, i

            if max_ending_here < 0:
                max_ending_here = 0
                # start of the new partial substring when the current substring becomes zero
                post_start_idx = i+1

        return w[pre_start_idx:end_idx+1]


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        w = input()
        n = int(input())
        x = input().split(' ')
        b = input().split(' ')
        for itr in range(n):
            b[itr] = int(b[itr])

        ob = Solution()
        print(ob.maxSum(w, x, b, n))
# } Driver Code Ends
