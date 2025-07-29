<h1 align="center">Find duplicate rows in a binary matrix</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 60.19%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 37K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>boolean</b> matrix of size <b>RxC</b> where each cell contains either 0 or 1, find the row numbers (0-based) of row which already exists or are repeated.

<b>Example 1:</b>

<pre><b>Input:</b>
R = 2, C = 2
matrix[][] = {{1, 0},
            {1, 0}}
<b>Output: </b>
1
<b>Explanation:</b>
Row 1 is duplicate of Row 0.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
R = 4, C = 3
matrix[][] = {{ 1, 0, 0},
            { 1, 0, 0},
            { 0, 0, 0},
            { 0, 0, 0}}
<b>Output: </b>
1 3 
<b>Explanation:</b>
Row 1 and Row 3 are duplicates of Row 0 and 2 respectively. </pre>

<b>Your Task:</b><br>You dont need to read input or print anything. Complete the function <b>repeatedRows()</b> that takes the matrix as input parameter and returns a list of row numbers which are duplicate rows.

<b>Expected Time Complexity:</b> O(R * C)<br><b>Expected Auxiliary Space:</b> O(R * C) 

<b>Constraints:</b><br>1 ≤ R, C ≤ 10<sup>3</sup><br>0 ≤ matrix[i][j] ≤ 1


<hr>

### Tags
- **Topic Tags:** `Matrix` `Trie` `Data Structures` `Advanced Data Structure`
- **Company Tags:** `Microsoft`

### Related Articles
- [Find Duplicate Rows Binary Matrix](https://www.geeksforgeeks.org/find-duplicate-rows-binary-matrix/)

### Related Interview Experiences
- [Microsoft Internship Interview Experience 3](https://www.geeksforgeeks.org/microsoft-internship-interview-experience-3/)
