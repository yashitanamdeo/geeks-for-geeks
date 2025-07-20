<h1 align="center">Shortest Source to Destination Path</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 24.69%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 121K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a 2D binary matrix A(0-based index) of dimensions NxM. Find the minimum number of steps required to reach from (0,0) to (X, Y).<br>Note: You can only move left, right, up and down, and only through cells that <b>contain 1</b>.

<b>Example 1:</b>

<pre><b>Input:</b>
N=3, M=4
A=[[1,0,0,0], 
   [1,1,0,1],<br>   [0,1,1,1]]
X=2, Y=3 
<b>Output:</b>
5
<b>Explanation:</b>
The shortest path is as follows:
(0,0)->(1,0)->(1,1)->(2,1)->(2,2)->(2,3).</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N=3, M=4
A=[[1,1,1,1],
   [0,0,0,1],<br>   [0,0,0,1]]
X=0, Y=3
<b>Output:</b>
3
<b>Explanation:</b>
The shortest path is as follows:
(0,0)->(0,1)->(0,2)->(0,3).</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>shortestDistance()</b> which takes the integer N, M, X, Y, and the 2D binary matrix A as input parameters and returns the minimum number of steps required to go from (0,0) to (X, Y).If it is impossible to go from (0,0) to (X, Y),then function returns -1. If value of the cell (0,0) is 0 (i.e  A[0][0]=0) then return -1.

<b>Constraints:</b><br>1 <= N,M <= 250<br>0 <= X < N<br>0 <= Y < M<br>0 <= A[i][j] <= 1

## Expected Complexities
- Time Complexity: O(n * m)
- Auxiliary Space: O(n * m)

<hr>

### Tags
- **Topic Tags:** `DFS` `Matrix` `Graph` `BFS` `Data Structures` `Algorithms`
- **Company Tags:** `Samsung`

### Related Articles
- [Shortest Path In A Binary Maze](https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/)
