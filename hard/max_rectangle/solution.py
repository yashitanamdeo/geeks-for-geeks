# Problem Statement: https://www.geeksforgeeks.org/problems/max-rectangle/1

class Solution:
    def maxArea(self, mat):
        def largestHistogramArea(heights):
            # Add sentinel zeros to simplify edge handling
            heights = [0] + heights + [0]
            stack = []
            max_area = 0

            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)

            return max_area

        if not mat or not mat[0]:
            return 0

        max_area = largestHistogramArea(mat[0])

        for i in range(1, len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    mat[i][j] += mat[i - 1][j]
            max_area = max(max_area, largestHistogramArea(mat[i]))

        return max_area
