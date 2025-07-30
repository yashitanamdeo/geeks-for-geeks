<h1 align="center">Zero Sum Subarrays</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.49%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 142K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 60m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array <b>arr[]</b> of integers. Find the total count of subarrays with their sum equal to 0.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [0, 0, 5, 5, 0, 0]
<b>Output: </b>6<b>
Explanation: </b>The 6 subarrays are [0], [0], [0], [0], [0,0], and [0,0].</pre>

<pre><b>Input: </b>arr[] = [6, -1, -3, 4, -2, 2, 4, 6, -12, -7]
<b>Output: </b>4<b>
Explanation: </b>The 4 subarrays are [-1, -3, 4], [-2, 2], [2, 4, 6, -12], <br>and [-1, -3, 4, -2, 2]
</pre>

<pre><b>Input: </b>arr[] = [0]
<b>Output: </b>1<b>
Explanation: </b>The only subarray is [0].</pre>

<b>Constraints:    </b><br>1 <= n <= 10<sup>6</sup><br>-10<sup>9</sup> <= arr[ i ] <= 10<sup>9</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Hash` `Data Structures`
- **Company Tags:** `Amazon` `Microsoft` `OYO Rooms`

### Related Articles
- [Print All Subarrays With 0 Sum](https://www.geeksforgeeks.org/print-all-subarrays-with-0-sum/)
