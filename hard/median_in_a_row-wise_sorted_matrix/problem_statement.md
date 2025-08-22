<h1 align="center">Median in a row-wise sorted Matrix</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 55.05%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 158K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>row-wise sorted</b> matrix <b>mat[][]</b> of size n*m, where the number of rows and columns is always <b>odd</b>. Return the <b>median</b> of the matrix.

<b>Examples:</b>

<pre><b>Input</b>: mat[][] = [[1, 3, 5], <br>                [2, 6, 9], <br>                [3, 6, 9]]
<b>Output:</b> 5
<b>Explanation</b>: Sorting matrix elements gives us [1, 2, 3, 3, 5, 6, 6, 9, 9]. Hence, 5 is median.
</pre>

<pre><b>Input: </b>mat[][] = [[2, 4, 9],
                [3, 6, 7],
                [4, 7, 10]]
<b>Output: </b>6
<b>Explanation</b>: Sorting matrix elements gives us [2, 3, 4, 4, 6, 7, 7, 9, 10]. Hence, 6 is median.</pre>

<pre><b>Input: </b>mat = [[3], [4], [8]]
<b>Output: </b>4
<b>Explanation</b>: Sorting matrix elements gives us [3, 4, 8]. Hence, 4 is median.<br></pre>

<b>Constraints:</b><br>1 ≤ n, m ≤ 400<br>1 ≤ mat[i][j] ≤ 2000

## Expected Complexities
- Time Complexity: O(n log m * log(maxVal – minVal))
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Matrix` `Binary Search` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find Median Row Wise Sorted Matrix](https://www.geeksforgeeks.org/find-median-row-wise-sorted-matrix/)
