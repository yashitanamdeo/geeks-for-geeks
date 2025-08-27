# Problem Statement: https://www.geeksforgeeks.org/problems/count-possible-triangles-1587115620/1

class Solution:
    def countTriangles(self, arr):
        arr.sort()
        n = len(arr)
        count = 0
        
        # Fix the largest side (arr[k]) and find pairs (i,j) such that arr[i] + arr[j] > arr[k]
        for k in range(2, n):  # k starts from 2 (third element)
            i = 0
            j = k - 1  # j starts from element just before k
            
            while i < j:
                if arr[i] + arr[j] > arr[k]:
                    # If arr[i] + arr[j] > arr[k], then arr[i+1] + arr[j] > arr[k], 
                    # arr[i+2] + arr[j] > arr[k], ..., arr[j-1] + arr[j] > arr[k]
                    # So we can form (j-i) triangles
                    count += (j - i)
                    j -= 1  # Try with smaller second element
                else:
                    i += 1  # Try with larger first element
        
        return count