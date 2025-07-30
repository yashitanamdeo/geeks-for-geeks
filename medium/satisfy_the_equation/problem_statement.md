<h1 align="center">Satisfy the equation</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.31%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 15K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>A[ ]</b> of <b>N</b> of  integers, find the distinct index of values that satisfy<b> A + B = C + D</b> where <b>A,B,C</b> & <b>D</b> are integers values in the array.<br><b>Note: </b>As there may be multiple pairs satisfying the equation return lexicographically smallest order of  A, B, C and D and return all as -1 if there are no pairs satisfying the equation.

 

<b>Example 1:</b>

<pre><b>Input:</b>
<b>N = </b>7
<b>A[] = </b>{3, 4, 7, 1, 2, 9, 8}
<b>Output:</b>
0 2 3 5
<b>Explanation:</b>
A[0] + A[2] = 3+7 = 10
A[3] + A[5] = 1+9 = 10</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
<b>N = </b>4
<b>A[] = </b>{424, 12, 31, 7}
<b>Output:</b>
-1 -1 -1 -1
<b>Explanation:</b>
There are no pairs satisfying the equation.</pre>

 

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>satisfyEqn()</b> which takes an Integer N and an array A[] of size N as input and returns a vector of 4 integers denoting A, B, C, and D respectively.

 

<b>Expected Time Complexity:</b> O(N<sup>2</sup>*logN<sup>2</sup>)<br><b>Expected Auxiliary Space:</b> O(N<sup>2</sup>)

 

<b>Constraints:</b><br>1 <= N <= 500<br>1 <= A[i] <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Hash` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Find Four Elements A B C And D In An Array Such That Ab Cd](https://www.geeksforgeeks.org/find-four-elements-a-b-c-and-d-in-an-array-such-that-ab-cd/)
