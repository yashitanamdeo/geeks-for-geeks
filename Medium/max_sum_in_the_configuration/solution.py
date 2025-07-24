# Problem Statement: https://www.geeksforgeeks.org/problems/max-sum-in-the-configuration/1

#User function Template for python3

def max_sum(a, n):
    # Calculate the initial sum and the total sum of the array
    S0 = sum(i * a[i] for i in range(n))
    sumA = sum(a)
    
    # Initialize the maximum sum
    max_sum_value = S0
    current_sum = S0
    
    # Iterate over the array to find the maximum sum possible by rotating
    for k in range(1, n):
        current_sum = current_sum + sumA - n * a[n - k]
        if current_sum > max_sum_value:
            max_sum_value = current_sum
    
    return max_sum_value

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends