# Problem Statement: https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

#{ 
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        n=len(arr)
        l,h,mid=0,n-1,0
        while mid<=h:
            if arr[mid]==0:
                arr[mid],arr[l]=arr[l],arr[mid]
                mid+=1
                l+=1
            elif arr[mid]==1:
                mid+=1
            else:
                arr[mid],arr[h]=arr[h],arr[mid]
                h-=1
            

#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")
        
if __name__ == "__main__":
    main()

# } Driver Code Ends