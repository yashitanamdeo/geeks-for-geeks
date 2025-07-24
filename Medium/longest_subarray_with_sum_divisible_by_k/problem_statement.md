<h1 align="center">Longest subarray with sum divisible by K</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 33.72%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 103K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b> and a positive integer <b>k</b>, find the length of the <b>longest </b>subarray with the sum of the elements <b>divisible </b>by <b>k</b>.<br><b>Note: </b>If there is no subarray with sum divisible by k, then return 0.<br>

<b>Examples :</b>

<pre><b>Input: </b>arr[] = [2, 7, 6, 1, 4, 5], k = 3
<b>Output:</b> 4
<b>Explanation: </b>The subarray [7, 6, 1, 4] has sum = 18, which is divisible by 3.</pre>

<pre><b>Input: </b>arr[] = [-2, 2, -5, 12, -11, -1, 7], k = 3
<b>Output:</b> 5
<b>Explanation: </b>The subarray [2, -5, 12, -11, -1] has sum = -3, which is divisible by 3.<br></pre>

<pre><b>Input: </b>arr[] = [1, 2, -2], k = 2
<b>Output:</b> 2
<b>Explanation: </b>The subarray is [2, -2] has sum = 0, which is divisible by 2.</pre>

<b>Constraints:</b><br>1 <= arr.size() <= 10<sup>6</sup><br>1 <= k <= 10<sup>6</sup><br>-10<sup>6</sup> <= arr[i] <= 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(min(n, k))

<hr>

### Tags
- **Topic Tags:** `prefix-sum` `Arrays` `Hash` `Data Structures` `Algorithms`
- **Company Tags:** `Microsoft` `Snapdeal`

### Related Articles
- [Longest Subarray Sum Divisible K](https://www.geeksforgeeks.org/longest-subarray-sum-divisible-k/)
