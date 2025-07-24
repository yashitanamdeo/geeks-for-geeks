<h1 align="center">Making A Large Island</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 52.36%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 41K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an<b> n x n </b>binary matrix<b> grid[][]</b>. You are allowed to change at most one<b> 0</b> to <b>1</b>. A group of <b>connected 1s</b> forms an island. Two 1s are connected if they share one of their sides with each other.

Return the size of the <b>largest island</b> in the grid after applying this operation.

<b>Examples:</b>

<pre><b>Input: </b>grid[] = [[1,0],[0,1]]<br><b>Output: </b>3<br><b>Explanation: </b>Change any one 0 to 1 and connect two 1s, then we get an island with area = 3.</pre>

<pre><b>Input: </b>grid[] = [[1,1],[1,0]]<br><b>Output: </b>4<br><b>Explanation: </b>Change the only 0 to 1 and make the island bigger, then we get an island with area = 4.</pre>

<pre><b>Input: </b>grid[] = [[1,1],[1,1]]<br><b>Output: </b>4<br><b>Explanation: </b>Can't change any 0 to 1, only one island possible with area = 4.</pre>

<b>Constraints:</b>

1 <= n <= 500<br>0 <= grid[i][j] <= 1


<hr>

### Tags
- **Topic Tags:** `Matrix` `DFS` `BFS` `union-find`
- **Company Tags:** `Intuit`

### Related Articles
- [Find Length Largest Region Boolean Matrix](https://www.geeksforgeeks.org/find-length-largest-region-boolean-matrix/)
