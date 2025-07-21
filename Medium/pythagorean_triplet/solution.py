# Problem Statement: https://www.geeksforgeeks.org/problems/pythagorean-triplet3018/1

#User function Template for python3
class Solution:
    def checkTriplet(self, arr, n):
        # Create a dictionary to store the square of each element as keys
        # and the corresponding original element as values.
        square_map = {i * i: i for i in arr}

        # Iterate through the square_map to find triplets with the sum of squares.
        for square1 in square_map:
            for square2 in square_map:
                # Calculate the sum of two squared values.
                sum_of_squares = square1 + square2

                # Check if the sum exists in the square_map, indicating the presence of a triplet.
                if sum_of_squares in square_map:
                    return True

        # If no triplet is found, return False.
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends