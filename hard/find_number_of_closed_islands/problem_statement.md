<h1 align="center">Find number of closed islands</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 61.43%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 27K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a [binary matrix](https://www.geeksforgeeks.org/program-to-check-if-a-matrix-is-binary-matrix-or-not/) <b>mat[][]</b> of dimensions <b>NxM</b> such that 1 denotes land and <b>0</b> denotes water. Find the number of closed islands in the given matrix.<br>An island is a 4-directional(up,right,down and left) connected part of 1's.

<b>Note:</b> A closed island is a group of <b>1s</b> surrounded by only <b>0s</b> on all the boundaries <b>(except diagonals)</b>. In simple words, a closed island is an island whose none of the <b>1s</b> lie on the edges of the matrix.

<b>Example 1:</b>

<pre><b>Input:</b>
N = 5, M = 8
mat[][] = {{0, 0, 0, 0, 0, 0, 0, 1}, 
           {0, 1, 1, 1, 1, 0, 0, 1}, 
           {0, 1, 0, 1, 0, 0, 0, 1}, 
           {0, 1, 1, 1, 1, 0, 1, 0}, 
           {1, 0, 0, 0, 0, 1, 0, 1}}
<b>Output:</b>
2
<b>Explanation</b>:
mat[][] = {{0, 0, 0, 0, 0, 0, 0, 1}, 
           {0, <b>1, 1, 1, 1, </b>0, 0, 1}, 
           {0, <b>1</b>, 0, <b>1</b>, 0, 0, 0, 1}, 
           {0, <b>1, 1, 1, 1, </b>0, <b>1</b>, 0}, 
           {1, 0, 0, 0, 0, 1, 0, 1}} 
There are 2 closed islands. The islands in dark are closed because they are completely surrounded by 0s (water). There are two more islands in the last column of the matrix, but they are not completely surrounded by 0s. Hence they are not closed islands. 
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N = 3, M = 3
mat[][] = {{1, 0, 0},
           {0, 1, 0},
           {0, 0, 1}}
<b>Output: <br></b>1<b><br>Explanation:<br></b>mat[][] = {{1, 0, 0},<br>          {0, <b>1</b>, 0},<br>          {0, 0, 1}}<br>There is just a one closed island.</pre>

<b>Your task:</b><br>You dont need to read input or print anything. Your task is to complete the function <b>closedIslands()</b> which takes two integers N and M, and a 2D binary matrix mat as input parameters and returns the number of closed islands.

<b>Expected Time Complexity: </b>O(N*M)<br><b>Expected Auxiliary Space: </b>O(N*M)

<b>Constraints:</b><br>1 ≤ N,M ≤ 500<br><br>


<hr>

### Tags
- **Topic Tags:** `DFS` `Matrix` `Graph` `BFS` `union-find` `Data Structures` `Algorithms`
- **Company Tags:** `Google`

### Related Articles
- [Find Number Of Closed Islands In Given Matrix](https://www.geeksforgeeks.org/find-number-of-closed-islands-in-given-matrix/)
