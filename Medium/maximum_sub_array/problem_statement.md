<h1 align="center">Maximum Sub Array</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 15.84%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 113K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of integers <b>arr[]</b>, find the contiguous subarray with the <b>maximum sum </b>that contains only non-negative numbers. If multiple subarrays have the same sum, return the one with the <b>smallest starting index</b>. If the array contains only <b>negative</b> numbers, return <b>-1</b>.

<b>Note: </b>A subarray is a contiguous non-empty sequence of elements within an array.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [1, 2, 3]
<b>Output:</b> [1, 2, 3]
<b>Explanation:</b> In the given array, every element is non-negative, so the entire array [1, 2, 3] is the valid subarray with the maximum sum.
</pre>

<pre><b>Input: </b>arr[] = [-1, 2]
<b>Output:</b> [2]
<b>Explanation:</b> The only valid non-negative subarray is [2], so the output is [2].<br></pre>

<pre><b>Input: </b>arr[] = [1, 2, 5, -7, 2, 6]
<b>Output:</b> [1, 2, 5]
<b>Explanation:</b> The valid non-negative subarrays are [1, 2, 5] and [2, 6]. Both have the same sum of 8, but [1, 2, 5] starts earlier, so it is the preferred subarray.</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>6</sup><br>-10<sup>5 </sup>≤ arr[i] ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Divide and Conquer` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon` `Microsoft` `Intuit`

### Related Articles
- [Largest Sum Contiguous Subarray Having Only Non Negative Elements](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray-having-only-non-negative-elements/)

### Related Interview Experiences
- [Intuit Interview Experience Set 12](https://www.geeksforgeeks.org/intuit-interview-experience-set-12/)
