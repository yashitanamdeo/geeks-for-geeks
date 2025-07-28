<h1 align="center">Make Matrix Beautiful</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 64.75%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 64K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

A <b>beautiful matrix</b> is defined as a square matrix in which the <b>sum </b>of elements in every row and every column is equal. Given a square matrix <b>mat[][]</b>, your task is to determine the <b>minimum number of operations</b> required to make the matrix beautiful.<br>In one operation, you are allowed to increment the value of <b>any single cell </b>by<b> 1</b>.

<b>Examples:</b>

<pre><b>Input</b>: mat[][] = [[1, 2], <br>                [3, 4]]
<b>Output</b>: 4
<b>Explanation</b>:<br>Increment value of cell(0, 0) by 3, <br>Increment value of cell(0, 1) by 1. <br>Matrix after the operations: [[4, 3], <br>                            [3, 4]]<br>Here, sum of each row and column is 7.<br>Hence total 4 operation are required.
</pre>

<pre><b>Input</b>: mat[][] = [[1, 2, 3],<br>                [4, 2, 3],<br>                [3, 2, 1]]
<b>Output</b>: 6
<b>Explanation</b>: <br>Increment value of cell(0, 0) by 1, <br>Increment value of cell(0, 1) by 2, <br>Increment value of cell(2, 1) by 1, <br>Increment value of cell(2, 2) by 2. <br>Matrix after the operations: [[2, 4, 3], <br>                            [4, 2, 3],<br>                            [3, 3, 3]] <br>Here, sum of each row and column is 9.<br>Hence total 6 operation are required.</pre>

<b>Constraints:</b><br>1 ≤ mat.size() ≤ 900<br>0 ≤ mat[i][j] ≤ 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Matrix` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Minimum Operations Required Make Row Column Matrix Equals](https://www.geeksforgeeks.org/minimum-operations-required-make-row-column-matrix-equals/)
