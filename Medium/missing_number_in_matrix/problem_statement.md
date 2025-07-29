<h1 align="center">Missing number in matrix</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.0%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 19K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a matrix of size <b>n x n</b> such that it has only <b>one</b> <b>0</b>, Find the <b>positive number</b> (greater than zero) to be placed in place of the 0 such that sum of the numbers in every row, column and two diagonals become equal. If no such number exists, return -1.

<b>Note:</b> Diagonals should be only of the form matrix[i][i] and matrix[i][n-i-1]. <b>n</b> is always greater than 1. The <b>answer</b> can be greater than <b>10<sup>9</sup></b>. <br> 

<b>Example 1:</b>

<pre><b>Input: </b>matrix = {{5, 5}, {5, 0}}
<b>Output: </b>5
<b>Explanation: </b>The matrix is
5 5
5 0
Therefore If we place 5 instead of 0, all
the element of matrix will become 5. 
Therefore row 5+5=10, column 5+5=10 and 
diagonal 5+5=10, all are equal.</pre>

<b>Example 2:</b>

<pre><b>Input: </b>matrix = {{1, 2, 0}, {3, 1, 2}, 
{2, 3, 1}}
<b>Output: </b>-1
<b>Explanation: </b>It is not possible to insert 
an element in place of 0 so that the 
condition is satisfied.thus result is -1. 

</pre>

<b>Your Task:</b><br>You don't need to read or print anyhting. Your task is to complete the function <b>MissingNo() </b>which takes the matrix as input parameter and returns the number which should be placed in place of 0 such that the condition gets satisfied. If not possible return -1.<br> 

<b>Expected Time Complexity: </b>O(n * n)<br><b>Expected Space Complexity: </b>O(2 * n)<br> 

<b>Constraints:</b><br>2 <= n <= 1000<br>1 <= elements in the matrix <= 10^9


<hr>

### Tags
- **Topic Tags:** `Matrix` `Data Structures`
- **Company Tags:** `None`
