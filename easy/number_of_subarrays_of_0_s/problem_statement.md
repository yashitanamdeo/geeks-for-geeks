<h1 align="center">Number of Subarrays of 0's</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 56.17%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 26K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array <b>arr</b>  of length<b> N</b> of 0's and 1's. Find the total number of subarrays of 0's

<b>Example 1:</b>

<pre><b>Input:
</b>N = 4
arr[] = {0, 0, 1, 0}
<b>Output:</b>
4
<b>Explanation:</b>
Following are the subarrays of
length 1: {0}, {0}, {0} - 3
length 2: {0, 0} - 1
Total Subarrays: 3 + 1 = 4</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N = 4
arr[] = {0, 0, 0, 0}
<b>Output:</b>
10
<b>Explanation:</b>
Following are the subarrays of
length 1: {0}, {0}, {0}, {0} - 4
length 2: {0, 0}, {0, 0}, {0, 0} - 3
length 3: {0, 0, 0}, {0, 0, 0} - 2
length 4: {0, 0, 0, 0} - 1
Total Subarrays: 4 + 3 + 2 + 1 = 10
</pre>

<b>Your Task:</b>

Your task is to complete the function <b>no_of_subarrays(),</b> which takes an integer <b>N </b>and an integer array <b>arr </b>as the input parameters and returns an integer denoting the total number of subarrays of 0's.

<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b>

- 1 <= N <= 10<sup>6</sup>
- 0 <= arr[i] <= 1


<hr>

### Tags
- **Topic Tags:** `Arrays`
- **Company Tags:** `None`

### Related Articles
- [Find The Total Number Of Subarrays Of 0s](https://www.geeksforgeeks.org/find-the-total-number-of-subarrays-of-0s/)
