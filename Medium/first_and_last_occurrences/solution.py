# Problem Statement: https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1

#User function Template for python3


class Solution:
    def find(self, sorted_array, length, target):
        """
        Find the first and last occurrence indices of the target in a sorted array.

        :param sorted_array: A sorted array of integers.
        :param length: The length of the array.
        :param target: The target integer to search for.
        :return: A tuple containing the first and last occurrence indices (or -1 if not found).
        """

        def find_first_occurrence(array, length, target):
            left, right = 0, length - 1
            first_occurrence = -1

            while left <= right:
                mid = left + (right - left) // 2

                if array[mid] == target:
                    first_occurrence = mid
                    right = mid - 1
                elif array[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return first_occurrence

        def find_last_occurrence(array, length, target):
            left, right = 0, length - 1
            last_occurrence = -1

            while left <= right:
                mid = left + (right - left) // 2

                if array[mid] == target:
                    last_occurrence = mid
                    left = mid + 1
                elif array[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return last_occurrence

        first_occurrence = find_first_occurrence(sorted_array, length, target)
        last_occurrence = find_last_occurrence(sorted_array, length, target)
        return (first_occurrence, last_occurrence)


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends