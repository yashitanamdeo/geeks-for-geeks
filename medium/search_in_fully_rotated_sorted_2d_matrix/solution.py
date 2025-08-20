# Problem Statement: https://www.geeksforgeeks.org/problems/search-in-fully-rotated-sorted-2d-matrix/1

class Solution:
    def searchMatrix(self, mat, x):
        for arr in mat:
            if arr[-1]<arr[0]:
                if x in arr:
                    return True
            elif x>=arr[0] and x<=arr[-1]:
                if x in arr:
                    return True
        return False