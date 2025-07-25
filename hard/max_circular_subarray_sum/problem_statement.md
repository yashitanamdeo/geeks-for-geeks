<h1 align="center">Max Circular Subarray Sum</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 29.37%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 172K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 25m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a circular array <b>arr[] </b>of integers, find the <b>maximum</b> possible sum of a non-empty <b>subarray</b>. In a circular array, the subarray can start at the end and wrap around to the beginning. Return the maximum non-empty subarray sum, considering both non-wrapping and wrapping cases.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [8, -8, 9, -9, 10, -11, 12]
<b>Output: </b>22<b>
Explanation: </b>Starting from the last element of the array, i.e, 12, and moving in a circular fashion, we have max subarray as 12, 8, -8, 9, -9, 10, which gives maximum sum as 22.</pre>

<pre><b>Input: </b>arr[] = [10, -3, -4, 7, 6, 5, -4, -1]
<b>Output: </b>23<b>
Explanation: </b>Maximum sum of the circular subarray is 23. The subarray is [7, 6, 5, -4, -1, 10].<br></pre>

<pre><b>Input: </b>arr[] = [5, -2, 3, 4]<br><b>Output: </b>12<b>
Explanation: </b>The circular subarray [3, 4, 5] gives the maximum sum of 12.</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>5</sup><br>-10<sup>4 </sup>≤ arr[i] ≤ 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures` `Kadane` `Algorithms`
- **Company Tags:** `Amazon` `Microsoft`

### Related Articles
- [Maximum Contiguous Circular Sum](https://www.geeksforgeeks.org/maximum-contiguous-circular-sum/)
