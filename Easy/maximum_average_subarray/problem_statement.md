<h1 align="center">Maximum average subarray</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 42.11%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 15K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>a</b><b>rr</b> of size <b>n</b> and a positive integer <b>k</b>, find the subarray of length <b>k</b> with the maximum average. <b>You need to</b> <b>return the starting index of the subarray</b>. If there are multiple subarrays with the same maximum average, <b>return the smallest starting index</b>.

<br><b>Example 1:</b>

<pre><b>Input:
</b>k = 4, n = 6
arr[] = {1, 12, -5, -6, 50, 3}
<b>Output:</b> 12 -5 -6 50
<b>Explanation:</b> Maximum average is (12 - 5 - 6 + 50)/4 = 51/4.</pre>

<br><b>Example 2:</b>

<pre><b>Input:
</b>k = 3, n = 7
arr[] = {3, -435, 335, 10, -50, 100, 20}
<b>Output:</b> 335 10 -50
<b>Explanation:</b> Maximum average is (335 + 10 - 50)/3 = 295/3.
</pre>

<br><b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>findMaxAverage()</b> which takes the array of integers <b>arr, </b>its size <b>n</b> and integer <b>k </b>as input parameters and returns an integer denoting the starting index of the subarray.

<br><b>Expected Time Complexity:</b> O(n)<br><b>Expected Auxiliary Space:</b> O(1)<br><br><b>Constraints</b><br>1 <= k <= n <= 10<sup>5</sup><br>0 <= |arr[i]| <= 10<sup>3</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Find Maximum Average Subarray Of K Length](https://www.geeksforgeeks.org/find-maximum-average-subarray-of-k-length/)
