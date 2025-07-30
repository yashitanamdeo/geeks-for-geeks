<h1 align="center">Number Of Islands</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 60.65%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 58K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a <b>n,m</b> which means the row and column of the 2D matrix and an array of  size k denoting the number of operations. Matrix elements is 0 if there is water or 1 if there is land. Originally, the 2D matrix is all 0 which means there is no land in the matrix. The array has k operator(s) and each operator has two integer A[i][0], A[i][1] means that you can change the cell matrix[A[i][0]][A[i][1]] from sea to island. Return how many island are there in the matrix after each operation.You need to return an array of size <b>k</b>.<br>
<b>Note : </b>An island means group of 1s such that they share a common side.

 

<b>Example 1:</b>

<pre><b>Input:</b> n = 4
m = 5
k = 4
A = {{1,1},{0,1},{3,3},{3,4}}

<b>Output:</b> 1 1 2 2
<b>Explanation:</b>
0.  00000
    00000
    00000
    00000
1.  00000
    01000
    00000
    00000
2.  01000
    01000
    00000
    00000
3.  01000
    01000
    00000
    00010
4.  01000
    01000
    00000
    00011</pre>

 

 

<b>Example 2:</b>

<pre><b>Input:</b> n = 4
m = 5
k = 4
A = {{0,0},{1,1},{2,2},{3,3}}

<b>Output:</b> 1 2 3 4
<b>Explanation:</b>
0.  00000
    00000
    00000
    00000
1.  10000
    00000
    00000
    00000
2.  10000
    01000
    00000
    00000
3.  10000
    01000
    00100
    00000
4.  10000
    01000
    00100
    00010</pre>

 

<b>Your Task:</b><br>
You don't need to read or print anything. Your task is to complete the function numOfIslands() which takes an integer n denoting no. of rows in the matrix, an integer m denoting the number of columns in the matrix and a 2D array of size k denoting  the number of operators.

<b>Expected Time Complexity:</b> O(m * n)<br>
<b>Expected Auxiliary Space:</b> O(m * n)

<b>Constraints:</b>

1 <= n,m <= 100<br>
1 <= k <= 1000


<hr>

### Tags
- **Topic Tags:** `union-find` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find The Number Of Islands Using Dfs](https://www.geeksforgeeks.org/find-the-number-of-islands-using-dfs/)
