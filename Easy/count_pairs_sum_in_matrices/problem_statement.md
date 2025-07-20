<h1 align="center">Count pairs Sum in matrices</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 45.66%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 58K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two matrices <b>mat1[][]</b> and <b>mat2[][]</b> of size n x n, where the elements in each matrix are arranged in strictly <b>ascending order</b>. Specifically, <b>each row</b> is sorted from <b>left to right</b>, and the last element of a row is <b>smaller</b> than the first element of the next row. <br>You're given a target value <b>x</b>, your task is to find and <b>count</b><b> </b>all pairs <b>{a, b} </b>such that <b>a </b>is from <b>mat1 </b>and <b>b </b>is from <b>mat2 </b>where the sum of <b>a +</b> <b>b</b> is equal to <b>x</b>.

<b>Examples:</b>

<pre><b>Input:</b> n = 3, x = 21,<br>mat1[][] = [[1, 5, 6], [8, 10, 11], [15, 16, 18]],
mat2[][] = [[2, 4, 7], [9, 10, 12], [13, 16, 20]]
<b>OUTPUT: </b>4
<b>Explanation: </b>The pairs whose sum is found to be 21 are (1, 20), (5, 16), (8, 13) and (11, 10).</pre>

<pre><b>Input: </b>n = 2, x = 10,
mat1[][] = [[1, 2], [3, 4]]
mat2[][] = [[4, 5], [6, 7]]
<b>Output: </b>2
<b>Explanation: </b>The pairs whose sum found to be 10 are (4, 6) and (3, 7).</pre>

<b>Constraints:<br></b>1 ≤ n ≤ 100<br>1 ≤ x ≤ 10<sup>5</sup><br>1 ≤ mat1[i][j] , mat2[i][j] ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Hash` `Sorting` `Matrix` `Data Structures` `Algorithms`
- **Company Tags:** `FactSet`

### Related Articles
- [Count Pairs Two Sorted Matrices Given Sum](https://www.geeksforgeeks.org/count-pairs-two-sorted-matrices-given-sum/)
