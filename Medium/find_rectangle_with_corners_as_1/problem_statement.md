<h1 align="center">Find rectangle with corners as 1</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 56.75%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 21K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an <b>n x m</b> binary matrix <b>mat[][]</b> containing only 0s and 1s, determine if there exists a rectangle within the matrix such that all four corners of the rectangle are 1. If such a rectangle exists, return <b>true</b>; otherwise, return <b>false</b>.

<b>Example:</b>

<pre><b>Input: </b>mat[][] =<br>[[1, 0, 0, 1, 0],
[0, 0, 1, 0, 1],
[0, 0, 0, 1, 0], 
[1, 0, 1, 0, 1]] 
<b>Output</b>: true
<b>Explanation: </b>Valid corners are at index (1,2), (1,4), (3,2), (3,4) </pre>

<pre><b>Input: </b>mat[][] =<br>[[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]
<b>Output: </b>false<br><b>Explanation: </b>There are no valid corners.</pre>

<b>Constraints:</b><br>1 <= n, m <= 200<br>0 <= mat[i] <= 1

## Expected Complexities
- Time Complexity: O(n * (m^2))
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Matrix` `Data Structures`
- **Company Tags:** `Flipkart`

### Related Articles
- [Find Rectangle Binary Matrix Corners 1](https://www.geeksforgeeks.org/find-rectangle-binary-matrix-corners-1/)

### Related Interview Experiences
- [Flipkart Interview Experience For Sde Internship On Campus 2021](https://www.geeksforgeeks.org/flipkart-interview-experience-for-sde-internship-on-campus-2021/)
