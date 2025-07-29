<h1 align="center">Number of paths</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 67.64%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 121K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a grid of size <b>m x n</b>, the task is to determine the number of distinct paths from the <b>top-left corner</b> to the <b>bottom-right corner</b>. At each step, one can either move down or right. Given the integers m and n, return the number of unique paths from the top-left corner to the bottom-right corner.

Note: The test cases are designed such that the answer will always fit within a 32-bit integer.

<b>Examples:</b>

<pre><b>Input</b>: m = 3, n = 3
<b>Output:</b> 6
<b>Explanation</b>: Let the given input 3*3 grid is filled as such:
A B C
D E F
G H I
The possible unique paths which exists to reach 'I' from 'A' following above conditions are as follows: ABCFI, ABEHI, ADGHI, ADEFI, ADEHI, ABEFI.</pre>

<pre><b>Input</b>: m = 2, n = 3
<b>Output</b>: 3
<b>Explanation</b>: Let the given input 2*3 grid is filled as such:
A B C
D E F
The possible unique paths which exists to reach 'F' from 'A' following above conditions are as follows: ABCF, ADEF and ABEF.
</pre>

<pre><b>Input</b>: m = 1, n = 4
<b>Output:</b> 1
<b>Explanation</b>: Let the given input 1*4 grid is filled as such:<br>A B C D <br>The only possible unique path is ABCD.</pre>

<b>Constraints:</b><br>1 ≤ m ≤ 100<br>1 ≤ n ≤ 100

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(n^2)

<hr>

### Tags
- **Topic Tags:** `Algorithms` `Dynamic Programming`
- **Company Tags:** `Zoho` `Amazon` `Microsoft`

### Related Articles
- [Count Possible Paths Top Left Bottom Right Nxm Matrix](https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/)
