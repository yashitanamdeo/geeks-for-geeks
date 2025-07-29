<h1 align="center">Shortest Path by Removing K walls</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.4%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 22K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 40m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a 2-D binary <b>matrix</b> of size <b>n*m</b>, where 0 represents an empty space while 1 represents a wall you cannot walk through. You are also given an integer <b>k</b>.<br>
You can walk up, down, left, or right. Given that you can remove up to <b>k</b> walls, return the minimum number of steps to walk from the top left corner (0, 0) to the bottom right corner (n-1, m-1).<br>
<b>Note: </b>If there is no way to walk from the top left corner to the bottom right corner, return -1.

<br>
<b>Example 1:</b>

<pre><b>Input: </b>n = 3, m = 3, k = 1
mat = {{0, 0, 0},
       {0, 0, 1},
       {0, 1, 0}}
<b>Output:
</b>4<b>
Explanation:
</b>We can remove any one of the walls and
reach the bottom in 4 moves.  
</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>n = 2, m = 2, k = 0
mat[] = {{0, 1},
         {1, 0}}
<b>Output:
</b>-1<b>
Explanation:
</b>There's no way of reaching the bottom
corner without removing any walls.
</pre>

<br>
<b>Your Task:</b><br>
The task is to complete the function <b>shotestPath</b>() which takes three integers n, m, and k and also a matrix of size n*m as input and returns the minimum number of steps to walk from the top left corner to the bottom right corner.

<br>
<b>Constraints:</b><br>
1 ≤ n,m ≤ 50<br>
0 ≤ k ≤ n*m<br>
Top left and bottom right corners doesn't have 1

<br>
<b>Expected Time Complexity: </b>O(n*m*k).<br>
<b>Expected Auxiliary Space: </b>O(n*m*k).


<hr>

### Tags
- **Topic Tags:** `Matrix` `BFS` `Data Structures` `Algorithms`
- **Company Tags:** `Google`

### Related Articles
- [Shortest Path By Removing K Walls](https://www.geeksforgeeks.org/shortest-path-by-removing-k-walls/)
