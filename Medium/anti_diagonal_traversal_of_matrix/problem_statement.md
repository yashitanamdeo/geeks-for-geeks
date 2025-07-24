<h1 align="center">Anti Diagonal Traversal of Matrix</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 73.72%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 30K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 40m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Give a N*N square <b>matrix</b>, return an array of its <b>anti-diagonals </b>in top-leftmost to bottom-rightmost order. In an element of a <b>anti-diagonal (i, j)</b>, surrounding elements will be <b>(i+1, j-1)</b> and <b>(i-1, j+1)</b>. Look at the examples for more clarity.

<b>Example 1:</b>

<pre><b>Input:</b>
N = 2
matrix[][] = 1 2<br>            3 4
<b>Output:</b>
1 2 3 4
<b>Explanation:</b>
List of anti-diagnoals in order is<br>{1}, {2, 3}, {4}</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N = 3
matrix[][] = 3 2 3<br>            4 5 1<br>            7 8 9<br><b>Output:</b>
3 2 4 3 5 7 1 8 9</pre>

<pre><b>Explanation:</b>
List of anti-diagnoals in order is<br>{3}, {2, 4}, {3, 5, 7}, {1, 8}, {9}</pre>

<b>Your Task:</b><br>You dont need to read input or print anything. Complete the function <b>antiDiagonal</b><b>Pattern()</b> that takes <b>matrix </b>as input parameter and returns a <b>list of integers </b>in order of the values visited in the anti-Diagonal pattern. 

<b>Expected Time Complexity:</b> O(N * N)<br><b>Expected Auxiliary Space:</b> O(N * N)<br> 

<b>Constraints:</b><br>1 <= N <= 100<br>0 <= mat[i][j] <= 100


<hr>

### Tags
- **Topic Tags:** `Misc` `Matrix` `Data Structures`
- **Company Tags:** `Amazon` `Microsoft`

### Related Articles
- [0](https://www.geeksforgeeks.org/0/)
