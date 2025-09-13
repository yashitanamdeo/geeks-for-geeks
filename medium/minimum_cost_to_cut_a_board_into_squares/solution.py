# Problem Statement: https://www.geeksforgeeks.org/problems/minimum-cost-to-cut-a-board-into-squares/1

class Solution:
    def minCost(self, n, m, x, y):
        n -= 1
        m -= 1
        x.sort(reverse=True)
        y.sort(reverse=True)
        x_i = y_i = cost = 0
        rows_count = cols_count = 1
        while x_i < m and y_i < n:
            if x[x_i] > y[y_i]:
                cost += x[x_i] * rows_count
                cols_count += 1
                x_i += 1
            else:
                cost += y[y_i] * cols_count
                rows_count += 1
                y_i += 1
        if x_i < m:
            cost += rows_count * sum(x[x_i:])
        elif y_i < n:
            cost += cols_count * sum(y[y_i:])
        return cost