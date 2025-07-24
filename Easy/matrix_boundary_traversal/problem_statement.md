<h1 align="center">Matrix Boundary Traversal</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 35.32%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 108K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a matrix <b>mat</b>. The task is to perform boundary traversal on the matrix in a clockwise manner starting from the first row of the matrix. <br><br><b>Examples:</b>

<pre><b>Input</b>: mat[][] = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15,16]]
<b>Output</b>: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5]
<b>Explanation</b>: The boundary traversal is: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5]
</pre>

<pre><b>Input</b>:mat[][] = [[12, 11, 10, 9],[8, 7, 6, 5],[4, 3, 2, 1]]
<b>Output</b>: [12, 11, 10, 9, 5, 1, 2, 3, 4, 8]<br><b>Explanation</b>: The boundary traversal is: [12, 11, 10, 9, 5, 1, 2, 3, 4, 8]</pre>

<pre><b>Input</b>:mat[][] = [[12, 11],[4, 3]]
<b>Output</b>: [12, 11, 3, 4]<br><b>Explanation</b>: The boundary traversal is: [12, 11, 3, 4]</pre>

<pre><b>Constraints:</b><br>1 <= mat.size()<= 1000<br>1 <= mat[0].size()<= 1000<br>0 <= mat[i][j] <= 1000</pre>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Matrix` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Boundary Elements Matrix](https://www.geeksforgeeks.org/boundary-elements-matrix/)
- [Java Program To Print Boundary Elements Of The Matrix](https://www.geeksforgeeks.org/java-program-to-print-boundary-elements-of-the-matrix/)
