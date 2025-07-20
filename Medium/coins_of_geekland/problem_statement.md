<h1 align="center">Coins of Geekland</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.38%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 9K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

In Geekland there is a grid of coins of size <b>N x</b> <b>N</b>. You have to find the maximum sum of coins in any sub-grid of size<b> K x K</b>.<br><b>Note:</b> Coins of the negative denomination are also possible at Geekland.<br><br><b>Example 1:</b>

<pre><b>Input: </b>N = 5, K = 3 
mat[[]] = {1, 1, 1, 1, 1} 
          {2, 2, 2, 2, 2} 
          {3, 8, 6, 7, 3} 
          {4, 4, 4, 4, 4} 
          {5, 5, 5, 5, 5}
<b>Output:</b> 48
<b>Explanation:</b> {8, 6, 7}
             {4, 4, 4}
             {5, 5, 5}
has the maximum sum
</pre>

<br><b>Example 2:</b>

<pre><b>Input: </b>N = 1, K = 1
mat[[]] = {{4}} 
<b>Output:</b> 4
</pre>

<b>Your Task: </b> <br>You don't need to read input or print anything. Complete the function <b>Maximum_Sum()</b> which takes the matrix mat[], size of Matrix N, and value K as input parameters and returns the maximum sum.

<b>Expected Time Complexity:</b> O(N<sup>2</sup>)<br><b>Expected Auxiliary Space:</b> O(N<sup>2</sup>)

<b>Constraints:</b><br>1 ≤ K ≤ N ≤ 10<sup>3</sup><br>-5*10<sup>5</sup> ≤ mat[i][j] ≤ 5*10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Matrix` `Data Structures`
- **Company Tags:** `Adobe`

### Related Articles
- [Print Maximum Sum Square Sub Matrix Of Given Size](https://www.geeksforgeeks.org/print-maximum-sum-square-sub-matrix-of-given-size/)
