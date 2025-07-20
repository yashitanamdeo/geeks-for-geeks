<h1 align="center">Matrix Operations</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 63.42%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 6K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary matrix of dimensions <b>M * N. </b>One can perform the given operation in the matrix.

- If the value of <b>matrix[i][j]</b> is <b>0</b>, then traverse in the same direction and check the next value.
- If the value of <b>matrix[i][j]</b> is <b>1</b>, then update <b>matrix[i][j]</b> to <b>0</b> and change the current direction from <b>up</b>, <b>right</b>, <b>down</b>, or <b>left</b> to the directions <b>right</b>, <b>down</b>, <b>left</b>, and <b>up</b> respectively.
Initially you start from <b>cell(0, 0)</b>, moving in <b>right</b> direction.

The task is to find the first cell of the matrix  which leads to outside the matrix from the traversal of the given matrix from the cell <b>(0, 0)</b> by performing the operations.

<b>Example 1:</b>

<pre><b>Input:</b>
matrix[][] = {{0,1},
              {1,0}}

<b>Output:</b> (1,1)
<b>Explanation:</b>




</pre>

<b>Example 2:</b>

<pre><b>Input:</b> 
matrix[][] = {{0, 1, 1, 1, 0},
                   {1, 0, 1, 0, 1},
              {1, 1, 1, 0, 0}}

<b>Output:</b> (2,0)</pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. Complete the function <b>endPoints()</b> that take the matrix as input parameter and output the last cell before the pointer gets outside of the matrix.

<b>Constrains:</b><br>
1<= M, N <=1000<br>
0<= matrix[i][j] <=1


<hr>

### Tags
- **Topic Tags:** `Matrix` `Data Structures`
- **Company Tags:** `Samsung`

### Related Articles
- [Coordinates Of The Last Cell In A Matrix On Which Performing Given Operations Exits From The Matrix](https://www.geeksforgeeks.org/coordinates-of-the-last-cell-in-a-matrix-on-which-performing-given-operations-exits-from-the-matrix/)
