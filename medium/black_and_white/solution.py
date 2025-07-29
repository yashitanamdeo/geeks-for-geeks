# Problem Statement: https://practice.geeksforgeeks.org/problems/black-and-white-1587115620/1

#User function Template for python3


#Function to find out the number of ways we can place a black and a white
#Knight on this chessboard such that they cannot attack each other.
import sys
import io
import atexit


def numOfWays(M, N):

    sum = 0
    for i in range(N):
        for j in range(M):
            count = 0
            for new_i, new_j in [(i+1, j+2), (i+1, j-2), (i-1, j+2), (i-1, j-2), (i+2, j+1), (i+2, j-1), (i-2, j+1), (i-2, j-1)]:
                if new_i < N and new_i >= 0 and new_j < M and new_j >= 0:
                    count += 1
            sum += N*M - 1 - count
            sum %= 1000000007

    return sum


#{
 # Driver Code Starts
#Initial Template for Python 3


# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m, n = map(int, input().strip().split())
        print(numOfWays(m, n))

# } Driver Code Ends
