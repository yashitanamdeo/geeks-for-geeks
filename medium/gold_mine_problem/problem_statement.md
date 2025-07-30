<h1 align="center">Gold Mine Problem</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 29.73%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 137K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a gold mine called <b>mat[][]</b>. Each field in this mine contains a <b>positive integer </b>which is the amount of gold in tons. Initially, the miner can start from any <b>row</b> in the first <b>column</b>. From a given cell, the miner can move -

1. to the cell diagonally up towards the right
1. to the right
1. to the cell diagonally down towards the right
Find out the <b>maximum amount of gold </b>that he can collect until he can no longer move.

<b>Examples:</b>

<pre><b>Input:</b> mat[][] = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]
<b>Output:</b> 12
<b>Explaination:</b> The path is (1, 0) -> (2, 1) -> (2, 2). Total gold collected is 2 + 6 + 4 = 12.</pre>

<pre><b>Input: </b>mat[][] = [[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]
<b>Output:</b> 16
<b>Explaination:</b> The path is (2, 0) -> (3, 1) -> (2, 2) -> (2, 3) or (2, 0) -> (1, 1) -> (1, 2) -> (0, 3). <br>Total gold collected is (5 + 6 + 2 + 3) or (5 + 2 + 4 + 5) = 16.<br></pre>

<pre><b>Input:</b> mat[][] = [[1, 3, 3], [2, 1, 4], [0, 7, 5]]
<b>Output:</b> 14
<b>Explaination:</b> The path is (1,0) -> (2,1) -> (2,2). Total gold collected is 2 + 7 + 5 = 14.</pre>

<b>Constraints:</b><br>1 ≤ mat.size(), mat[0].size() ≤ 500<br>0 ≤ mat[i][j] ≤ 100

## Expected Complexities
- Time Complexity: O(n * m)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Flipkart` `Amazon` `Samsung`

### Related Articles
- [Gold Mine Problem](https://www.geeksforgeeks.org/gold-mine-problem/)

### Related Interview Experiences
- [Samsung Rd Bangalore Interview Experience For Internship 2021 On Campus](https://www.geeksforgeeks.org/samsung-rd-bangalore-interview-experience-for-internship-2021-on-campus/)
- [Flipkart Interview Set 2 Sde 2](https://www.geeksforgeeks.org/flipkart-interview-set-2-sde-2/)
