<h1 align="center">Sum of upper and lower triangles</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 71.0%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 73K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a square matrix<b> </b>of size<b> n*n</b>, print the <b>sum of upper and lower triangular elements</b>. Upper Triangle consists of elements on the diagonal and above it. The lower triangle consists of elements on the diagonal and below it. <br><br><b>Examples:</b>

<pre><b>Input</b>:n = 3,mat[][] = [[6, 5, 4],
                    [1, 2, 5],
                    [7, 9, 7]]
<b>Output</b>: [29, 32]
<b>Explanation</b>:The given matrix is
6 5 4
1 2 5
7 9 7</pre>

<pre>Upper triangular matrix:
6 5 4
  2 5
    7
Sum of these elements is 6 + 5 + 4 + 2 + 5 + 7=29.</pre>

<pre>Lower triangular matrix:
6
1 2
7 9 7
Sum of these elements is 6 + 1 + 2 + 7 + 9 + 7= 32.</pre>

<pre><b>Input</b>:n = 2, mat[][] = [[1, 2],
                     [3, 4]]
<b>Output</b>: [7, 8]
<b>Explanation:</b>Upper triangular matrix:
1 2
  4
Sum of these elements are 7.
Lower triangular matrix:
1
3 4
Sum of these elements are 8.</pre>

<br><b>Constraints:</b> <br>1 <= n <= 10<sup>3</sup><br>1 <= mat[i][j] <= 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Matrix` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Sum Upper Triangle Lower Triangle](https://www.geeksforgeeks.org/sum-upper-triangle-lower-triangle/)
