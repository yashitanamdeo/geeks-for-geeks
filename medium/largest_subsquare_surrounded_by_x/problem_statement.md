<h1 align="center">Largest subsquare surrounded by X</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.31%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 38K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a square matrix<b> mat[][]</b>, where each cell can be either '<b>X</b>' or '<b>O</b>', you need to find the size of the <b>largest square subgrid</b> that is completely surrounded by '<b>X</b>'. More formally you need to find the largest square within the grid where all its <b>border cells are 'X'</b>.

<b>Examples:</b>

<pre><b>Input: </b>mat[][] = [[X,X],[X,X]]
<b>Output: </b>2
<b>Explanation: </b>The largest square submatrix surrounded by X is the whole input matrix.</pre>

<pre><b>Input: </b>mat[][] = [[X,X,X,O],[X,O,X,X],[X,X,X,O],[X,O,X,X]]
<b>Output: </b>3
<b>Explanation:</b>
Here,the input represents following 
matrix of size 4 x 4
<b>X</b> <b>X</b> <b>X</b> O
<b>X</b> O <b>X</b> X
<b>X</b> <b>X</b> <b>X</b> O
X O X X
The square submatrix starting at (0,0) and ending at (2,2) is the largest submatrix surrounded by X. Therefore, size of that matrix would be 3.</pre>

<b>Constraints:</b><br>1 <= mat.size() <= 1000<br>

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(n^2)

<hr>

### Tags
- **Topic Tags:** `Matrix` `Data Structures`
- **Company Tags:** `D-E-Shaw`

### Related Articles
- [Given Matrix O X Find Largest Subsquare Surrounded X](https://www.geeksforgeeks.org/given-matrix-o-x-find-largest-subsquare-surrounded-x/)
