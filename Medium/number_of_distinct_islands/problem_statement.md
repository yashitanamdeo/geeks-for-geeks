<h1 align="center">Number of Distinct Islands</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 62.29%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 107K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a boolean 2D matrix <b>grid </b>of size <b>n</b> * <b>m</b>. You have to find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. Two islands are considered to be distinct if and only if one island is not equal to another (not rotated or reflected).

<b>Example 1:</b>

<pre><b>Input:</b>
grid[][] = {{1, 1, 0, 0, 0},
            {1, 1, 0, 0, 0},
            {0, 0, 0, 1, 1},
            {0, 0, 0, 1, 1}}
<b>Output:</b>
1
<b>Explanation:</b>
grid[][] = {{1, 1, 0, 0, 0}, 
            {1, 1, 0, 0, 0}, 
            {0, 0, 0, 1, 1}, 
            {0, 0, 0, 1, 1}}
Same colored islands are equal.
We have 2 equal islands, so we 
have only 1 distinct island.

</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
grid[][] = {{1, 1, 0, 1, 1},
            {1, 0, 0, 0, 0},
            {0, 0, 0, 0, 1},
            {1, 1, 0, 1, 1}}
<b>Output:</b>
3
<b>Explanation:
</b>grid[][] = {{1, 1, 0, 1, 1}, 
            {1, 0, 0, 0, 0}, 
            {0, 0, 0, 0, 1}, 
            {1, 1, 0, 1, 1}}
Same colored islands are equal.
We have 4 islands, but 2 of them
are equal, So we have 3 distinct islands.

</pre>

<b>Your Task:</b>

You don't need to read or print anything. Your task is to complete the function <b>countDistinctIslands() </b>which takes the <b>grid</b> as an input parameter and returns the total number of <b>distinct</b> islands.

<b>Expected Time Complexity: </b>O(n * m)<br>
<b>Expected Space Complexity: </b>O(n * m)

<b>Constraints:</b><br>
1 ≤ n, m ≤ 500<br>
grid[i][j] == 0 or grid[i][j] == 1


<hr>

### Tags
- **Topic Tags:** `DFS` `Graph` `BFS` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find The Number Of Distinct Islands In A 2d Matrix](https://www.geeksforgeeks.org/find-the-number-of-distinct-islands-in-a-2d-matrix/)
