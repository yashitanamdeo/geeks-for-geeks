<h1 align="center">Distinct Difference</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 64.7%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 21K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array A[] of length N. For each index, <b>i (1<=i<=N),</b> find the difference between the number of distinct elements in the left and right side in the of the current element in the array. 

<b>Example 1:</b>

<pre><b>Input</b>:
N = 3
arr[] = {4, 3, 3}
<b>Output:</b> {-1, 0, 2}
<b>Explanation</b>: For index i=1, there are 0 distinct element in the left side of it, and 1 distinct element(3) in it's right side. So difference is 0-1 = -1. 

Similarly for index i=2, there is 1 distinct element (4) in left side of it, and 1 distinct element(3) in it's right side. So difference is 1-1 = 0.

Similarly for index i=3, there are 2 distinct elements (4 and 3) in left side of it, and 0 distinct elements in it's left side. So difference is 2-0 = 2.

</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N = 4
arr[] = {4, 4, 3, 3}
<b>Output: </b>{-2, 0, 0, 2}
<b>Explanation</b>: For index i=1, there are 0 distinct element in the left side of it, and 2 distinct element(4 and 3) in it's right side. So difference is 0-2 = -2.

Similarly for index i=2, there is 1 distinct element (4) in left side of it, and 1 distinct element(3) in it's right side. So difference is 1-1 = 0.

Similarly for index i=4, there are 2 distinct elements (4 and 3) in left side of it, and 0 distinct element in it's right side. So difference is 2-0 = 2.</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>getDistinctDifference()</b> which takes the array A[] and its size N as input parameters and returns an array containing the difference between number of distinct elements in left and right side for each 1<=i<=N.

<b>Expected Time Complexity</b>: O(N)<br><b>Expected Space Complexity</b>: O(N)

<b>Constraints:</b>

1 <= N <= 10<sup>5</sup><br>1 <= A[i] <= 10<sup>9</sup><br>Array may contain duplicate elements.


<hr>

### Tags
- **Topic Tags:** `set` `Arrays` `Map` `Data Structures`
- **Company Tags:** `None`
