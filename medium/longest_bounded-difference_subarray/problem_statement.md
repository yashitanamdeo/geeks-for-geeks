<h1 align="center">Longest Bounded-Difference Subarray</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 58.27%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 26K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of positive integers <b>arr[] </b>and a non-negative integer <b>x</b>, the task is to find the <b>longest sub-array</b> where the absolute difference between any two elements is not greater than <b>x</b>. <br>If multiple such subarrays exist, return the one that starts at the <b>smallest index</b>.

<b>Examples:</b>

<pre><b>Input: </b>arr[] =<b> </b>[8, 4, 5, 6, 7], x = 3 <br><b>Output: </b>[4, 5, 6, 7] <br><b>Explanation: </b>The sub-array described by index [1..4], i.e. [4, 5, 6, 7]<br>contains no two elements whose absolute differnce is greater than 3.</pre>

<pre><b>Input:</b> arr[] =<b> </b>[1, 10, 12, 13, 14], x = 2 <br><b>Output: </b>[12, 13, 14] <br><b>Explanation: </b>The sub-array described by index [2..4], i.e. [12, 13, 14]<br>contains no two elements whose absolute differnece is greater than 2. </pre>

<b>Constraints:<br></b>1 ≤ arr.size() ≤ 10<sup>5<br></sup>1 ≤ arr[i] ≤ 10<sup>9<br></sup>0 ≤ x ≤ 10<sup>9</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Algorithms` `Heap` `sliding-window` `Arrays` `Queue` `Deque`
- **Company Tags:** `None`

### Related Articles
- [Longest Subarray In Which Absolute Difference Between Any Two Element Is Not Greater Than X](https://www.geeksforgeeks.org/longest-subarray-in-which-absolute-difference-between-any-two-element-is-not-greater-than-x/)
