<h1 align="center">Replace O's with X's</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 34.0%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 120K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a matrix <b>mat</b> where every element is either 'O' or 'X'. Replace all 'O' or a group of 'O' with 'X' that are surrounded by 'X'. 

A 'O' (or a set of 'O') is considered to be surrounded by 'X' if there are 'X' at locations just below, just above, just left and just right of it.

<b>Examples:</b>

<pre><b>Input:</b> mat = <br>[['X', 'X', 'X', 'X'], <br>['X', 'O', 'X', 'X'], <br>['X', 'O', 'O', 'X'], <br>['X', 'O', 'X', 'X'], <br>['X', 'X', 'O', 'O']]
<b>Output:</b> <br>[['X', 'X', 'X', 'X'], <br>['X', 'X', 'X', 'X'], <br>['X', 'X', 'X', 'X'], <br>['X', 'X', 'X', 'X'], <br>['X', 'X', 'O', 'O']]
<b>Explanation:</b> We only changed those 'O' that are surrounded by 'X'
</pre>

<pre><b>Input:</b> mat = <br>[['X', 'O', 'X', 'X'], <br>['X', 'O', 'X', 'X'], <br>['X', 'O', 'O', 'X'], <br>['X', 'O', 'X', 'X'], <br>['X', 'X', 'O', 'O']]
<b>Output:</b> <br>[['X', 'O', 'X', 'X'], <br>['X', 'O', 'X', 'X'], <br>['X', 'O', 'O', 'X'], <br>['X', 'O', 'X', 'X'], <br>['X', 'X', 'O', 'O']]
<b>Explanation:</b> There's no 'O' that's surround by 'X'.</pre>

<pre><b>Input:</b> mat = <br>[['X', 'X', 'X'], <br>['X', 'O', 'X'], <br>['X', 'X', 'X']]
<b>Output:</b> <br>[['X', 'X', 'X'], <br>['X', 'X', 'X'], <br>['X', 'X', 'X']]
<b>Explanation:</b> There's only one 'O' that's surround by 'X'.</pre>

<b>Constraints:</b><br>1 ≤ mat.size() ≤ 100<br>1 ≤ mat[0].size() ≤ 100<br>

## Expected Complexities
- Time Complexity: O(n * m)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Recursion` `Matrix` `Graph` `Data Structures` `Algorithms`
- **Company Tags:** `Google`

### Related Articles
- [Given Matrix O X Replace O X Surrounded X](https://www.geeksforgeeks.org/given-matrix-o-x-replace-o-x-surrounded-x/)
