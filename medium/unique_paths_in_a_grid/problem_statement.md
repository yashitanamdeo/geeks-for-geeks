<h1 align="center">Unique Paths in a Grid</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.47%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 55K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a 2d list <b>grid[][]</b> of size n x m consisting of values <b>0</b> and <b>1</b>.<br>A value of <b>0</b> means that you can enter that cell and <b>1</b> implies that entry to that cell is not allowed. <br>You start at the upper-left corner of the grid <b>(1, 1)</b> and you have to reach the bottom-right corner <b>(n, m)</b> such that you can only move in the<b> right</b> or <b>down</b> direction from every cell. <br>Your task is to calculate the total number of <b>ways</b> of reaching the target.<br>

<b>Note:</b> The <b>first (1, 1)</b> and <b>last (n, m) </b>cell of the grid can also be <b>1</b>.<br>It is guaranteed that the total number of ways<b> </b>will fit within a <b>32-bit</b> integer.<br><br><b>Examples:</b>

<pre><b>Input: </b>n = 3, m = 3,
grid[][] = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
<b>Output: </b>2
<b>Explanation: </b>There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down<br>2. Down -> Down -> Right -> Right</pre>

<pre><b>Input: </b>n = 1, m = 3,
grid[][] = [[1, 0, 1]]
<b>Output: </b>0
<b>Explanation: </b>There is no possible path to reach the end.
</pre>

<b>Constraints:</b><br>1 ≤ n*m ≤ 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n * m)
- Auxiliary Space: O(n * m)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Matrix` `Data Structures` `Algorithms`
- **Company Tags:** `Uber`

### Related Articles
- [Unique Paths In A Grid With Obstacles](https://www.geeksforgeeks.org/unique-paths-in-a-grid-with-obstacles/)

### Related Interview Experiences
- [Uber Interview Experience On Campus For Internship 2018 19](https://www.geeksforgeeks.org/uber-interview-experience-on-campus-for-internship-2018-19/)
