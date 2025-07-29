<h1 align="center">Rightmost different bit</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 61.61%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 122K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two integers <b>m</b> and <b>n </b>, return the position (1-based from the right) of the rightmost bit where they differ in binary, or -1 if both are identical.

<b>Examples: </b>

<pre><b>Input: </b>m = 11, n = 9
<b>Output:</b> 2
<b>Explanation:</b> Binary representation of the given numbers are: 1011 and 1001, 2nd bit from right is different.</pre>

<pre><b>Input: </b>m = 52, n = 4
<b>Output</b>: 5
<b>Explanation</b>: Binary representation of the given numbers are: 110100 and 0100, 5th-bit from right is different.<br></pre>

<pre><b>Input: </b>m = 29, n = 15
<b>Output</b>: 2
<b>Explanation</b>: Binary representation of the given numbers are: 29 in binary is 11101, 15 in binary is 01111. The 2nd bit from the right is different.</pre>

<b>Constraints:</b><br>0 ≤ m, n ≤ 10<sup>9</sup><br>

## Expected Complexities
- Time Complexity: max(log m, log n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Bit Magic` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Position Rightmost Different Bit](https://www.geeksforgeeks.org/position-rightmost-different-bit/)
