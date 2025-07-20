<h1 align="center">Boolean Matrix</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 40.05%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 125K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a boolean matrix <b>mat[],</b> where each cell contains either 0 or 1, modify it such that if a matrix cell matrix[i][j] is 1 then all the cells in its i<sup>th</sup> row and j<sup>th</sup> column will become 1.

<b>Examples:</b>

<pre><b>Input: </b>mat[][] = [[1, 0], [0, 0]]
<b>Output: </b>[[1, 1], [1, 0]] 
<b>Explanation: </b>Only cell that has 1 is at (0,0) so all cells in row 0 are modified to 1 and all cells in column 0 are modified to 1.</pre>

<pre><b>Input:</b> mat[][] = [[1, 0, 0], [1, 0, 0], [1, 0, 0], [0, 0, 0]]
<b>Output: </b>[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 0, 0]]
<b>Explanation: </b>The position of cells that have 1 in the original matrix are (0, 0), (1, 0) and (2, 0). Therefore, all cells in row 0, 1, 2 are and column 0 are modified to 1. </pre>

<pre><b>Input: </b>mat[][] = [[0, 0], [0, 0]]
<b>Output: </b>[[0, 0], [0, 0]] 
<b>Explanation: </b>There is no cell that contains 1, so mat[] will remain the same.</pre>

<b>Constraints:</b><br>1 ≤ mat.size(), mat[0].size() ≤ 10<sup>3</sup><br>0 ≤ mat[i][j] ≤ 1

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Matrix` `Data Structures`
- **Company Tags:** `Microsoft`

### Related Articles
- [A Boolean Matrix Question](https://www.geeksforgeeks.org/a-boolean-matrix-question/)

### Related Interview Experiences
- [Vmware Interview Experience Set 9 Internship Rd](https://www.geeksforgeeks.org/vmware-interview-experience-set-9-internship-rd/)
