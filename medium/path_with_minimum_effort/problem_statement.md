<h1 align="center">Path With Minimum Effort</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.13%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 52K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 25m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are a hiker preparing for an upcoming hike. You are given <b>heights[][]</b>, a 2D array of size <b>rows x columns</b>, where <b>heights[row][col]</b> represents the height of cell <b>(row, col)</b>. You are situated in the top-left cell, <b>(0, 0)</b>, and you hope to travel to the bottom-right cell, <b>(rows-1, columns-1)</b> (i.e., <b>0-indexed</b>). You can move <b>up</b>, <b>down</b>, <b>left</b>, or <b>right</b>, and you wish to find the route with minimum <b>effort</b>.

<b>Note: </b>A route's <b>effort</b> is the <b>maximum absolute difference</b><b> </b>in heights between two consecutive cells of the route.

<b>Example 1:</b>

<pre><b>Input:</b><br>row = 3<br>columns = 3 <br>heights = [[1,2,2],[3,8,2],[5,3,5]]
<b>Output:</b> <br>2
<b>Explanation:</b> <br>The route 1->3->5->3->5 has a maximum absolute difference of 2 in consecutive cells. This is better than the route 1->2->2->2->5, where the maximum absolute difference is 3.</pre>

<b>Example 2:</b>

<pre><b>Input:</b><br>row = 2<br>columns = 2 <br>heights = [[7,7],[7,7]]
<b>Output:</b> <br>0
<b>Explanation:</b> <br>Any route from the top-left cell to the bottom-right cell has a maximum absolute difference of 0 in consecutive cells.<br></pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>MinimumEffort() </b>which takes intergers <b>rows</b>, <b>columns,</b> and the 2D array <b>heights[][] </b><b> </b>and returns the<i> </i><b>minimum</b> <b>effort</b> required to travel from the top-left cell to the bottom-right cell<i>.</i>

<b>Expected Time Complexity: </b>O(rowsxcolumns)<br><b>Expected Space Complexity: </b>O(rowsxcolumns)

<b>Constraints:<br></b>1 <= rows, columns <= 100<b><br></b>rows == heights.length<br>
columns == heights[i].length<br>0 <= heights[i][j] <= 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Graph` `DFS` `BFS`
- **Company Tags:** `None`

### Related Articles
- [Path With Smallest Difference Between Consecutive Cells Path With Minimum Effort](https://www.geeksforgeeks.org/path-with-smallest-difference-between-consecutive-cells-path-with-minimum-effort/)
