<h1 align="center">Find the closest pair from two arrays</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 18.01%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 66K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two <b>sorted </b>arrays <b>arr</b> and <b>brr</b> and a number<b> x</b>, find the pair whose <b>sum</b> is closest to <b>x</b> and the pair has an element from<b> each</b> array. In the case of multiple closest pairs return any one of them.<br>Note: Can return the two numbers in any manner. The driver code takes care of the printing of the closest difference.

<b>Example 1:</b>

<pre><b>Input :</b> N = 4, M = 4<br>arr[ ] = {1, 4, 5, 7}
brr[ ] = {10, 20, 30, 40} 
X = 32
<b>Output :</b> <br>1, 30
<b>Explanation:</b>
The closest pair whose sum is closest
to 32 is {1, 30} = 31.
</pre>

<b>Example 2:</b>

<pre><b>Input :</b> N = 4, M = 4<br>arr[ ] = {1, 4, 5, 7}
brr[ ] = {10, 20, 30, 40}
X = 50 <b>
Output :</b> <br>7, 40 
<b>Explanation:</b> 
The closest pair whose sum is closest
to 50 is {7, 40} = 47.</pre>

<b>Your Task:</b><br>You only need to complete the function <b>printClosest()</b> that takes an array <b>(arr)</b>, another array <b>(brr)</b>, size of array arr <b>(N), </b>size of array brr <b>(M),</b> and return the array of two integers whose sum is closest to <b>X</b>. The driver code takes care of the printing of the closest difference.

<b>Expected Time Complexity:</b> O(N+M).<br><b>Expected Auxiliary Space:</b> O(1).

<b>Constraints:</b><br>1 ≤ N, M ≤ 10<sup>5</sup><br>1 ≤ A[i], B[i] ≤ 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Searching` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Given Two Sorted Arrays Number X Find Pair Whose Sum Closest X](https://www.geeksforgeeks.org/given-two-sorted-arrays-number-x-find-pair-whose-sum-closest-x/)
