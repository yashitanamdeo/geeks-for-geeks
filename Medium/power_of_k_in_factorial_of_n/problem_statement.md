<h1 align="center">Power of k in factorial of n</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.2%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 16K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two positive integers <b>n</b> and <b>k</b>, determine the highest value of <b>x</b> such that <b>k<sup>x</sup></b> <b>divides n! (n factorial) completely</b> (i.e., n % (k<sup>x</sup>) == 0).

<b>Examples :</b>

<pre><b>Input</b>: n = 7, k = 2
<b>Output:</b> 4
<b>Explanation</b>: 7! = 5040, and 2<sup>4 </sup>= 16 is the highest power of 2 that divides 5040.</pre>

<pre><b>Input: </b>n = 10, k = 9
<b>Output: </b>2
<b>Explanation</b>: 10! = 3628800, and 9² = 81 is the highest power of 9 that divides 3628800.</pre>

<b>Constraints:</b><br>1 ≤ n ≤ 10<sup>5</sup><br>2 ≤ k ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(sqrt(k) + m * log n), m = number of distinct prime factors in k
- Auxiliary Space: O(m), m = number of distinct prime factors in k

<hr>

### Tags
- **Topic Tags:** `number-theory` `Mathematical` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Largest Power K N Factorial K May Not Prime](https://www.geeksforgeeks.org/largest-power-k-n-factorial-k-may-not-prime/)
