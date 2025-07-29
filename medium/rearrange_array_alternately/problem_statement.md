<h1 align="center">Rearrange Array Alternately</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 35.15%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 259K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of <b>positive</b> integers. Your task is to rearrange the array elements alternatively i.e. first element should be the max value, the second should be the min value, the third should be the second max, the fourth should be the second min, and so on.<br><b>Note: </b>Modify the original array itself. Do it without using any extra space. You do not have to return anything.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [1, 2, 3, 4, 5, 6]
<b>Output: </b>[6, 1, 5, 2, 4, 3]<b>
Explanation: </b>Max element = 6, min = 1, second max = 5, second min = 2, and so on... The modified array is: [6, 1, 5, 2, 4, 3]</pre>

<pre><b>Input: </b>arr[]= [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
<b>Output: </b>[110, 10, 100, 20, 90, 30, 80, 40, 70, 50, 60]<b>
Explanation: </b>Max element = 110, min = 10, second max = 100, second min = 20, and so on... Modified array is : [110, 10, 100, 20, 90, 30, 80, 40, 70, 50, 60]
</pre>

<pre><b>Input: </b>arr[]= [1]
<b>Output: </b>[1]</pre>

<b>Constraints:</b><br>1 ≤ arr.size ≤ 10<sup>6</sup><br>1 ≤ arr[i] ≤ 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n log n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures`
- **Company Tags:** `Zoho`

### Related Articles
- [Rearrange Array Maximum Minimum Form Set 2 O1 Extra Space](https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form-set-2-o1-extra-space/)
- [Rearrange Array Maximum Minimum Form](https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form/)
