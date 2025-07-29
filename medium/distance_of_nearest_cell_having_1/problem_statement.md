<h1 align="center">Distance of nearest cell having 1</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 47.7%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 103K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary grid of <b>n*m</b>. Find the distance of the nearest 1 in the grid for each cell.<br>The distance is calculated as <b>|i<sub>1</sub>  - i<sub>2</sub>| + |j<sub>1</sub> - j<sub>2</sub>|</b>, where i<sub>1</sub>, j<sub>1</sub> are the row number and column number of the current cell, and i<sub>2</sub>, j<sub>2</sub> are the row number and column number of the nearest cell having value 1. There should be atleast one 1 in the grid.

<b>Examples</b>

<pre><b>Input: <br></b>grid = [[0,1,1,0], [1,1,0,0], [0,0,1,1]]
<b>Output: <br></b>[[1,0,0,1], [0,0,1,1], [1,1,0,0]]
<b>Explanation: <br></b>The grid is-
0 1 1 0 
1 1 0 0 
0 0 1 1 
- 0's at (0,0), (0,3), (1,2), (1,3), (2,0) and (2,1) are at a distance of 1 from 1's at (0,1), (0,2), (0,2), (2,3), (1,0) and (1,1) respectively.
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/701275/Web/Other/blobid0_1745302650.jpg" alt="" title="" width="183" height="162"/> </pre>

<pre><b>Input: <br></b>grid = [[1,0,1], [1,1,0], [1,0,0]]
<b>Output: <br></b>[[0,1,0], [0,0,1], [0,1,2]]
<b>Explanation:</b> <br>The grid is-
1 0 1
1 1 0
1 0 0
- 0's at (0,1), (1,2), (2,1) and (2,2) are at a  distance of 1, 1, 1 and 2 from 1's at (0,0), (0,2), (2,0) and (1,1) respectively.
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/701275/Web/Other/blobid1_1745302675.jpg" alt="" title="" width="196" height="173"/> </pre>

<b>Yout Task:</b><br>You don't need to read or print anything, Your task is to complete the function <b>nearest() </b>which takes the grid as an input parameter and returns a matrix of the same dimensions where the value at index (i, j) in the resultant matrix signifies the <b>minimum distance</b> of 1 in the matrix from grid[i][j].

<b>Constraints:</b><br>1 ≤ n, m ≤ 500

## Expected Complexities
- Time Complexity: O(n * m)
- Auxiliary Space: O(n * m)

<hr>

### Tags
- **Topic Tags:** `Matrix` `Graph` `BFS` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Distance Nearest Cell 1 Binary Matrix](https://www.geeksforgeeks.org/distance-nearest-cell-1-binary-matrix/)
