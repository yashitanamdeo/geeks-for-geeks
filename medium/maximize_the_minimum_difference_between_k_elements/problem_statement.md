<h1 align="center">Maximize the minimum difference between k elements</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 65.42%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 10K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b> of integers and an integer <b>k</b>, select k elements from the array such that the <b>minimum</b> <b>absolute difference</b> between any two of the selected elements is <b>maximized</b>. Return this <b>maximum</b> possible <b>minimum</b> difference.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [2, 6, 2, 5], k = 3<br><b>Output: </b>1<br><b>Explanation: </b>3 elements out of 4 elements are to be selected with a minimum difference as large as possible. Selecting 2, 2, 5 will result in minimum difference as 0. Selecting 2, 5, 6 will result in minimum difference as 6 - 5 = 1.</pre>

<pre><b>Input:</b> arr[] = [1, 4, 9, 0, 2, 13, 3], k = 4<br><b>Output:</b> 4<br><b>Explanation:</b> Selecting 0, 4, 9, 13 will result in minimum difference of 4, which is the largest minimum difference possible.</pre>

<b>Constraints:<br></b>1 ≤ arr.size()<b> </b>≤ 10<sup>5</sup><br>0 ≤ arr[i] ≤ 10<sup>6</sup><br>2 ≤ k ≤ arr.size()

## Expected Complexities
- Time Complexity: O(n log n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Binary Search` `Sorting` `Arrays`
- **Company Tags:** `None`

### Related Articles
- [Maximize The Minimum Difference Between Any Element Pair By Selecting K Elements From Given Array](https://www.geeksforgeeks.org/maximize-the-minimum-difference-between-any-element-pair-by-selecting-k-elements-from-given-array/)
