<h1 align="center">Sequence of Sequence</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 61.45%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 34K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 25m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two integers <b>n</b> and <b>m</b>, the task is to determine the total number of special sequences of length <b>n</b> such that:  

- seq[i+1] >= 2 * seq[i]
- seq[i] > 0
- seq[i] <= m
<b>Examples:</b>

<pre><b>Input:</b> n = 4, m = 10
<b>Output:</b> 4
<b>Explanation:</b> The sequences are {1, 2, 4, 8}, {1, 2, 4, 9}, {1, 2, 4, 10}, {1, 2, 5, 10}</pre>

<pre><b>Input:</b> n = 2, m = 5
<b>Output:</b> 6
<b>Explanation:</b> The sequences are {1, 2}, {1, 3}, {1, 4}, {1, 5}, {2, 4}, {2, 5}</pre>

<b>Constraints:</b><br>1 ≤ n ≤ 10<br>1 ≤ m ≤ 500

## Expected Complexities
- Time Complexity: O(n * m)
- Auxiliary Space: O(n * m)

<hr>

### Tags
- **Topic Tags:** `Divide and Conquer` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Sequences Given Length Every Element Equal Twice Previous](https://www.geeksforgeeks.org/sequences-given-length-every-element-equal-twice-previous/)
