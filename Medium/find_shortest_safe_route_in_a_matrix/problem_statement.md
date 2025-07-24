<h1 align="center">Find shortest safe route in a matrix</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.58%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 38K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a matrix <b>mat[][] with r </b>rows and <b>c </b>columns, where some cells are landmines <b>(marked as 0)</b> and others are safe to traverse. Your task is to <b>find the shortest safe route</b> from <b>any cell</b> in the leftmost column to <b>any cell</b> in the rightmost column of the <b>mat</b>. <b>You cannot move diagonally</b>, and you must <b>avoid both the landmines</b> and <b>their adjacent</b> cells (up, down, left, right), as they are also <b>unsafe</b>.

<b>Example 1:</b>

<pre><b>Input:</b>
mat = [1, 0, 1, 1, 1],
      [1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1],
      [1, 1, 1, 0, 1],
      [1, 1, 1, 1, 0]
<b>Output: <br></b>6
<b>Explanation: </b>
We can see that length of shortest
safe route is 6
[1 0 1 1 1]<br>[1 1 <b>1</b> <b>1</b> <b>1</b>]<br>[<b>1</b> <b>1</b> <b>1</b> 1 1]
[1 1 1 0 1] 
[1 1 1 1 0]
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
mat = [1, 1, 1, 1, 1],
      [1, 1, 0, 1, 1],
      [1, 1, 1, 1, 1]<b>
Output: <br></b>-1<b>
Explanation: </b>There is no possible path from
first column to last column.</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>findShortestPath() </b>which takes the matrix as an input parameter and returns an integer denoting the shortest safe path from <b>any cell</b> in the leftmost column to <b>any cell </b>in the rightmost column of <b>mat</b>. If there is no possible path, return <b>-1</b>. <br>

<b>Expected Time Complexity:</b> O(r * c)<br><b>Expected Auxiliary Space:</b> O(r * c)

<b>Constraints:</b><br>1 <= r, c <= 10<sup>3<br>0 <= mat[][] <= 1</sup>


<hr>

### Tags
- **Topic Tags:** `DFS` `Graph`
- **Company Tags:** `None`

### Related Articles
- [Find Shortest Safe Route In A Path With Landmines](https://www.geeksforgeeks.org/find-shortest-safe-route-in-a-path-with-landmines/)
