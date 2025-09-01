<h1 align="center">Sum of Mode</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.28%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 11K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b> of positive integers and an integer <b>k</b>. You have to find the sum of the <b>modes</b> of all the subarrays of size <b>k</b>.<br><b>Note:</b> The mode of a subarray is the element that occurs with the highest frequency. If multiple elements have the same highest frequency, the smallest such element is considered the mode.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [1, 2, 3, 2, 5, 2, 4, 4], k = 3<b><br>Output:</b> 13<b><br>Explanation:</b> The mode of each k size subarray is [1, 2, 2, 2, 2, 4] and sum of all modes is 13.</pre>

<pre><b>Input: </b>arr[] = [1, 2, 1, 3, 5], k = 2<b><br>Output:</b> 6<b><br>Explanation: </b>The mode of each k size subarray is [1, 1, 1, 3] and sum of all modes is 6.</pre>

<b>Constraints:<br></b>1 ≤ k ≤ arr.size() ≤10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n log k)
- Auxiliary Space: O(k)

<hr>

### Tags
- **Topic Tags:** `Greedy` `set` `sliding-window` `two-pointer-algorithm` `Hash`
- **Company Tags:** `None`

### Related Articles
- [Dsa](https://www.geeksforgeeks.org/dsa/mode-in-every-k-sized-window/)
