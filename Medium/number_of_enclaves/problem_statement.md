<h1 align="center">Number Of Enclaves</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.93%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 81K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an <b>n x m</b> binary matrix <b>grid</b>, where <b>0</b> represents a sea cell and <b>1</b> represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Find the number of land cells in <b>grid</b> for which we cannot walk off the boundary of the grid in any number of moves.

<b>Example 1:</b>

<pre><b>Input:</b>
grid[][] = {{0, 0, 0, 0},
            {1, 0, 1, 0},
            {0, 1, 1, 0},
            {0, 0, 0, 0}}
<b>Output:</b>
3
<b>Explanation:</b>
0 0 0 0
1 0 <b>1</b> 0
0 <b>1</b> <b>1</b> 0
0 0 0 0
The highlighted cells represents the land cells.
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
grid[][] = {{0, 0, 0, 1},
            {0, 1, 1, 0},
            {0, 1, 1, 0},
            {0, 0, 0, 1},
            {0, 1, 1, 0}}
<b>Output:</b>
4
<b>Explanation:</b>
0 0 0 1
0 <b>1</b> <b>1</b> 0
0 <b>1</b> <b>1</b> 0
0 0 0 1
0 1 1 0
The highlighted cells represents the land cells.</pre>

<b>Your Task:</b>

You don't need to print or input anything. Complete the function <b>numberOfEnclaves() </b>which takes a 2D integer matrix <b>grid </b>as the input parameter and returns an integer, denoting the number of land cells.

<b>Expected Time Complexity:</b> O(n * m)

<b>Expected Space Complexity:</b> O(n * m)

<b>Constraints:</b>

- 1 <= n, m <= 500
- grid[i][j] == 0 or 1


<hr>

### Tags
- **Topic Tags:** `DFS` `Matrix` `Graph` `BFS` `Data Structures` `Algorithms`
- **Company Tags:** `Google`

### Related Articles
- [Number Of Land Cells For Which We Cannot Walk Off The Boundary Of Grid](https://www.geeksforgeeks.org/number-of-land-cells-for-which-we-cannot-walk-off-the-boundary-of-grid/)
