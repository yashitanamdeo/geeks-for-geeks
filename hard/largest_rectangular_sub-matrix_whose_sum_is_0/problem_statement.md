<h1 align="center">Largest rectangular sub-matrix whose sum is 0</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 45.28%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 38K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a matrix <b>mat[][]</b>. Find the size of the largest sub-matrix whose <b>sum</b> is equal to <b>zero</b>. The size of a matrix is the product of rows and columns. A sub-matrix is a matrix obtained from the given matrix by deletion of several (possibly, zero or all) rows/columns from the beginning and several (possibly, zero or all) rows/columns from the end.

<b>Examples:</b>

<pre><b>Input: </b>mat[][] = [[9, 7, 16, 5], [1, -6, -7, 3], [1, 8, 7, 9], [7, -2, 0, 10]] <b>
Output: </b>6<b>
Explanation: <br></b><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/710026/Web/Other/blobid0_1736762643.png" alt="" title="" width="488" height="432"/></pre>

<pre><b>Input: </b>mat[][] =  [[1, 2, 3], [-3, -2, -1], [1, 7, 5]]
<b>Output:</b>  6
<b>Explanation:<br></b><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/710026/Web/Other/blobid1_1736762643.png" alt="" title="" width="478" height="426"/></pre>

<pre><b>Input:</b> mat[][] = [[1, -1], [-1, 1]]
<b>Output:</b> 4<br><b>Explanation:</b> The largest sub-matrix with sum 0 is [[1, -1], [-1, 1]].</pre>

<b>Constraints</b>:<br>1 <= mat.size(), mat[0].size() <= 100<br>-1000 <= mat[][] <= 1000

## Expected Complexities
- Time Complexity: O(n^3)
- Auxiliary Space: O(n^2)

<hr>

### Tags
- **Topic Tags:** `prefix-sum` `Hash` `Dynamic Programming` `Matrix` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Largest Rectangular Sub Matrix Whose Sum 0](https://www.geeksforgeeks.org/largest-rectangular-sub-matrix-whose-sum-0/)
