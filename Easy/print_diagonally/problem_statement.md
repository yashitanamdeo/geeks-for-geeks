<h1 align="center">Print Diagonally</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 66.11%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 40K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 10m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Give a <b>N * N</b> square matrix <b>A</b>, return all the elements of its anti-diagonals from <b>top to bottom</b>. 

<b>Example 1:</b>

<pre><b>Input:</b> 
N = 2
A = [[1, 2],
     [3, 4]]
<b>Output:</b>
1 2 3 4
<b>Explanation:</b> 

Hence, elements will be returned in the 
order {1, 2, 3, 4}.
</pre>

<b>Example 2:</b>

<pre><b>Input: 
</b>N = 3 
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
<b>Output:</b> 
1 2 4 3 5 7 6 8 9
<b>Explanation:</b> 

Hence, elements will be returned in 
the order {1, 2, 4, 3, 5, 7, 6, 8, 9}.

</pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>downwardDiagonal()</b> which takes an integer <b>N</b> and a 2D matrix <b>A[ ][ ]</b> as input parameters and returns the list of all elements of its anti-diagonals from <b>top to bottom</b>.

<b>Expected Time Complexity: </b>O(N*N)<br>
<b>Expected Auxillary Space: </b>O(N*N)

<b>Constraints:</b><br>
1 ≤ N, M ≤ 10<sup>3</sup><br>
0 ≤ A[i][j] ≤ 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Misc` `Matrix` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Print The Matrix Diagonally Downwards](https://www.geeksforgeeks.org/print-the-matrix-diagonally-downwards/)
