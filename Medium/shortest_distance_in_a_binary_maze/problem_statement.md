<h1 align="center">Shortest Distance in a Binary Maze</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 58.22%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 78K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>n * m</b> matrix <b>grid</b> where each element can either be <b>0</b> or <b>1</b>. You need to find the shortest distance between a given source cell to a destination cell. The path can only be created out of a cell if its value is 1. 

If the path is not possible between source cell and destination cell, then return <b>-1</b>.

<b>Note : </b>You can move into an adjacent cell if that adjacent cell is filled with element 1. Two cells are adjacent if they share a side. In other words, you can move in one of the four directions, Up, Down, Left and Right. The source and destination cell are based on the zero based indexing. The destination cell should be 1.

<b>Example 1:</b>

<pre><b>Input:</b>
grid[][] = {{1, 1, 1, 1},
            {1, 1, 0, 1},
            {1, 1, 1, 1},
            {1, 1, 0, 0},
            {1, 0, 0, 1}}
source = {0, 1}
destination = {2, 2}
<b>Output:</b>
3
<b>Explanation:</b>
1 <b>1</b> 1 1
1 <b>1</b> 0 1
1 <b>1</b> <b>1</b> 1
1 1 0 0
1 0 0 1
The highlighted part in the matrix denotes the 
shortest path from source to destination cell.
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
grid[][] = {{1, 1, 1, 1, 1},
            {1, 1, 1, 1, 1},
            {1, 1, 1, 1, 0},
            {1, 0, 1, 0, 1}}
source = {0, 0}
destination = {3, 4}
<b>Output:</b>
-1
<b>Explanation:</b>
The path is not possible between source and 
destination, hence return -1.
</pre>

<b>Your Task:</b>

You don't need to read or print anything. Your task is to complete the function <b>shortestPath() </b>which takes the a 2D integer array <b>grid</b>, <b>source</b> cell and <b>destination</b> cell as an input parameters and returns the shortest distance between source and destination cell.

<b>Expected Time Complexity: </b>O(n * m)<br><b>Expected Space Complexity: </b>O(n * m)

<b>Constraints:</b>

- 1 ≤ n, m ≤ 500
- grid[i][j] == 0 or grid[i][j] == 1
- The source and destination cells are always inside the given matrix.


<hr>

### Tags
- **Topic Tags:** `Matrix` `Graph` `BFS` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Shortest Path In A Binary Maze](https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/)
