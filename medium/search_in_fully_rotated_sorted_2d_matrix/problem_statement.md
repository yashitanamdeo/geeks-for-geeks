<h1 align="center">Search in fully rotated sorted 2D matrix</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 56.77%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 11K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a 2D matrix <b>mat[][] </b>of size n x m that was initially filled in the following manner:

 

- Each row is sorted in increasing order from left to right.
- The first element of every row is greater than the last element of the previous row.
 

This implies that if the matrix is flattened row-wise, it forms a strictly sorted 1D array.<br>Later, this sorted 1D array was rotated at some unknown pivot. The rotated array was then written back into the matrix row-wise to form the current matrix.

 

Given such a matrix <b>mat[][]</b> and an integer <b>x</b>, determine whether x exists in the matrix.

 

<b>Examples:<br></b>

<pre><b>Input: </b>x = 3,<b><br></b>mat[][] = [[7, 8, 9, 10],           
          [11, 12, 13, 1],
          [2, 3, 4, 5]] <b><br>Output: </b>true<b><br>Explanation: </b>3 is located at the 3rd row and 2nd column.</pre>

<pre><b>Input:</b> x = 10,<b><br></b>mat[][] <b>= </b>[[6, 7, 8],                         
          [9, 1, 2],
          [3, 4, 5]]<b><br>Output: </b>false<b><br>Explanation: </b>The value 10 does not exist in the matrix.</pre>

<b>Constraint:<br></b>1 ≤ n × m ≤ 10<sup>5</sup><br>1 ≤ mat[i][j], x ≤ 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(log(n * m))
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Binary Search` `Matrix` `Algorithms`
- **Company Tags:** `None`
