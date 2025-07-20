<h1 align="center">Number of paths in a matrix with k coins</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 16.96%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 57K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>n x n</b> matrix such that each of its cells contains some coins. Count the number of ways to collect <b>exactly k coins</b> while moving from top left corner of the matrix to the bottom right. From a cell (<b>i</b>, <b>j</b>), you can only move to (<b>i+1</b>, <b>j</b>) or (<b>i</b>, <b>j+1</b>).

<b>Example 1:</b>

<pre><b>Input</b>:
k = 12, n = 3
arr[] = [[1, 2, 3], 
       [4, 6, 5], 
       [3, 2, 1]]
<b>Output:</b> <br>2
<b>Explanation</b>: 
There are 2 possible paths with exactly 12 coins, (1 + 2 + 6 + 2 + 1) and (1 + 2 + 3 + 5 + 1).
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
k = 16, n = 3
arr[] = [[1, 2, 3], 
       [4, 6, 5], 
       [9, 8, 7]]
<b>Output: <br></b>0 
<b>Explanation: </b>
There are no possible paths that lead to sum=16
</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>numberOfPath()</b> which takes integers <b>n</b>, <b>k</b> and a 2D matrix <b>arr</b>[][] as input parameters and returns an integer denoting the number of possible paths.<br><br><b>Expected Time Complexity:</b> O(n*n*k)<br><b>Expected Auxiliary Space:</b> O(n*n*k)

<b>Constraints:<br></b>1 <= k < 100<br>1 <= n < 100<br>0 <= arr<sub>ij</sub> <= 200


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Recursion` `Matrix` `Backtracking` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon`

### Related Articles
- [Number Of Paths With Exactly K Coins](https://www.geeksforgeeks.org/number-of-paths-with-exactly-k-coins/)
