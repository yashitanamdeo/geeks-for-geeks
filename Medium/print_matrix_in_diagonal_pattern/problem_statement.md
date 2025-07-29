<h1 align="center">Print matrix in diagonal pattern</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 63.72%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 37K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a square matrix <b>mat[][]</b> of <b>n*n</b> size, the task is to determine the <b>diagonal pattern</b> which is a linear arrangement of the elements of the matrix as depicted in the following example:

<img src="https://contribute.geeksforgeeks.org/wp-content/uploads/matrix-6.png" alt="" title=""/>

<b>Example 1:</b>

<pre><b>Input:
</b>n = 3
mat[][] = {{1, 2, 3},<br>           {4, 5, 6},<br>           {7, 8, 9}}
<b>Output: {</b>1, 2, 4, 7, 5, 3, 6, 8, 9}<br><b>Explaination:<br></b>Starting from (0, 0): 1,
Move to the right to (0, 1): 2,
Move diagonally down to (1, 0): 4,
Move diagonally down to (2, 0): 7,<br>Move diagonally up to (1, 1): 5,
Move diagonally up to (0, 2): 3,
Move to the right to (1, 2): 6,
Move diagonally up to (2, 1): 8,
Move diagonally up to (2, 2): 9<br>There for the output is {1, 2, 4, 7, 5, 3, 6, 8, 9}.<br></pre>

<b>Example 2:</b>

<pre><b>Input:
</b>n = 2
mat[][] = {{1, 2},<br>           {3, 4}}
<b>Output: </b>{1, 2, 3, 4}<br><b>Explaination:</b><br>Starting from (0, 0): 1,
Move to the right to (0, 1): 2,
Move diagonally down to (1, 0): 3,
Move to the right to (1, 1): 4<br>There for the output is {1, 2, 3, 4}.</pre>

<b>Your Task:</b><br>You only need to implement the given function <b>matrixDiagonally() </b>which takes a matrix <b>mat[][]</b> of size <b>n*n</b> as an input and returns a list of integers containing the matrix diagonally. Do not read input, instead use the arguments given in the function.

<b>Expected Time Complexity:</b> O(n*n).<br><b>Expected Auxiliary Space:</b> O(n*n).

<b>Constraints:</b><br>1 <= n <= 100<br>-100 <= elements of matrix <= 100


<hr>

### Tags
- **Topic Tags:** `Matrix` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Print Matrix Diagonal Pattern](https://www.geeksforgeeks.org/print-matrix-diagonal-pattern/)
