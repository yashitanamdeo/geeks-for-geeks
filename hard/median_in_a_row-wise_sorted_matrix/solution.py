# Problem Statement: https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1

class Solution:
    def median(self, mat):
        #sam
        arr = []
        for i in mat:
            arr+=i
        arr.sort()
        mid = arr[len(arr)//2]
        return mid