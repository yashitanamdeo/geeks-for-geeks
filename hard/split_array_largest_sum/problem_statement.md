<h1 align="center">Split Array Largest Sum</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 58.9%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 61K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b> and an integer <b>k</b>, divide the array into <b>k</b> contiguous subarrays such that the <b>maximum </b>sum among these subarrays is <b>minimized</b>. Find this minimum possible <b>maximum sum</b>.<br>

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [1, 2, 3, 4], k = 3<b><br>Output: </b>4<b><br>Explanation: </b>Optimal Split is [1, 2], [3], [4]. Maximum sum of all subarrays is 4, which is minimum possible for 3 splits.<br></pre>

<pre><b>Input: </b>arr[] = [1, 1, 2], k = 2<br><b>Output: </b>2<br><b>Explanation: </b>Splitting the array as [1, 1] and [2] is optimal. This results in a maximum sum subarray of 2.</pre>

<b>Constraints:<br></b>1 ≤ k ≤ arr.size() ≤ 10<sup>5<br></sup>1 ≤ arr[i] ≤ 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n*log(sum))
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Binary Search` `Data Structures` `Algorithms`
- **Company Tags:** `Google`

### Related Articles
- [Split The Given Array Into K Sub Arrays Such That Maximum Sum Of All Sub Arrays Is Minimum](https://www.geeksforgeeks.org/split-the-given-array-into-k-sub-arrays-such-that-maximum-sum-of-all-sub-arrays-is-minimum/)
