<h1 align="center">Letters Collection</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 64.76%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 33K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

The Postmaster wants to write a program to answer the queries regarding letter collection in a city. A city is represented as a matrix <b>mat</b> of size<b> n*m.</b> Each cell represents a house and contains letters which are denoted by a number in the cell. The program should answer <b>q </b>queries which are of following types:<br><b>1 i j </b>: To sum all the letters which are at a 1-hop distance from the cell (i,j) in any direction<br><b>2 i j : </b>To sum all the letters which are at a 2-hop distance from the cell (i,j) in any direction <br>The queries are given in a 2D matrix <b>queries[][]</b>.<br>In one hop distance postmaster can go to any of [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)] from (i,j). 

<b>Example 1:</b>

<pre><b>Input:</b> 
n = 4, m = 5
mat = {{1, 2, 3, 4, 10}, 
       {5, 6, 7, 8, 10}, 
       {9, 1, 3, 4, 10}, 
       {1, 2, 3, 4, 10}}
q = 2
queries = {{1 0 1}, 
           {2 0 1}}
<b>Output:</b> <br>22 29
<b>Explaination:</b> 
For the first query sum is 1+5+6+7+3 = 22. 
For the second query sum is 9+1+3+4+8+4 = 29.<br></pre>

<b>Example 2:</b>

<pre><b>Input:</b> 
n = 6, m = 6
mat = {{ 1,  2,  3,  4,  5,  6}, 
       { 7,  8,  9, 10, 11, 12}, 
       {13, 14, 15, 16, 17, 18}, 
       {19, 20, 21, 22, 23, 24},<br>       {25, 26, 27, 28, 29, 30},<br>       {31, 32, 33, 34, 35, 36}}
q = 1
queries = {{2 3 2}}
<b>Output:</b> <br>336
<b>Explaination:</b> 
The first query sum is 7+8+9+10+11+17+23+29+35+34+33+32+31+25+19+13 = 336. </pre>

<b>Your Task:</b><br>You do not need to read input or print anything. Your task is to complete the function <b>matrixSum()</b> which takes <b>n</b>, <b>m</b>, <b>mat</b>, <b>q </b>and <b>queries </b>as input parameters and returns a list of integers where the ith value is the answers for ith query.

<b>Expected Time Complexity:</b> O(q)<br><b>Expected Auxiliary Space:</b> O(q)

<b>Constraints:</b><br>1 ≤ n, m ≤ 10<sup>3</sup><br>0 ≤ mat[i][j] ≤ 10<sup>7</sup><br>1 ≤ q ≤ 10<sup>5</sup><br>1 ≤ q[i][0] ≤ 2<br>0 ≤ q[i][1] < n<br>0 ≤ q[i][2] < m<br>


<hr>

### Tags
- **Topic Tags:** `Matrix` `CPP` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Postmaster Letters Collection](https://www.geeksforgeeks.org/postmaster-letters-collection/)
