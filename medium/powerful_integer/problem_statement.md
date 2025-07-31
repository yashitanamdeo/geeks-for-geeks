<h1 align="center">Powerful Integer</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.91%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 45K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a 2D integer array <b>intervals[][]</b> of length <b>n</b>, where each <b>intervals[i] = [start, end]</b> represents a closed interval (i.e., all integers from start to end, inclusive). You are also given an integer <b>k</b>. An integer is called <b>Powerful</b> if it appears in at least <b>k</b> intervals. Find the <b>maximum Powerful</b> Integer.

<b>Note</b>: If no integer occurs at least <b>k</b> times return <b>-1</b>.

<b>Examples:</b>

<pre><b>Input : </b>n = 3, intervals[][] = [[1, 3], [4, 6], [3, 4]], k = 2
<b>Output: </b>4
<b>Explanation: </b>Integers 3 and 4 appear in 2 intervals. The maximum is 4.</pre>

<pre><b>Input : </b>n = 4, intervals[][] = [[1, 4], [12, 45], [3, 8], [10, 12]], k = 3
<b>Output: </b>-1
<b>Explanation: </b>No integer appears in at least 3 intervals.
</pre>

<pre><b>Input : </b>n = 5, intervals[][] = [[16, 21], [5, 8], [12, 17], [17, 29], [9, 24]], k = 3
<b>Output: </b>21
<b>Explanation: </b>Integers 16, 17, 18, 19, 20 and 21 appear in at least 3 intervals. The maximum is 21.</pre>

<b>Constraints:</b><br>1 ≤ n ≤ 10<sup>5</sup><br>1 ≤ intervals[i][0] ≤ intervals[i][1] ≤ 10<sup>9</sup><br>1 ≤ k ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n log n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Hash` `Sorting` `Map` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Powerful Integers](https://www.geeksforgeeks.org/powerful-integers/)
