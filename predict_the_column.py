# Problem Statement: https://www.geeksforgeeks.org/problems/predict-the-column/1

#User function Template for python3

class Solution:
    def columnWithMaxZeros(self, matrix, N):
        min_non_zero_count, max_zero_column = float("inf"), -1

        for column_index in range(N):
            zero_count = 0
            for row_index in range(N):
                zero_count += matrix[row_index][column_index]

            if zero_count < N and min_non_zero_count > zero_count:
                min_non_zero_count, max_zero_column = zero_count, column_index

        return max_zero_column


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = []
        for i in range(N):
            line = [int(x) for x in input().strip().split()]
            arr.append(line)
        ob=Solution()
        print(ob.columnWithMaxZeros(arr,N))


# } Driver Code Ends
