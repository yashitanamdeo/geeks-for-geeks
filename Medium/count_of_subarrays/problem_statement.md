<h1 align="center">Count of Subarrays</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 48.53%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 34K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of <b>N</b> positive integers  <b>Arr<sub>1</sub>, Arr<sub>2</sub> ............ Arr<sub>n</sub></b>. The value of each contiguous subarray of given array is the <b>maximum element present in that subarray</b>. The task is to return the number of subarrays having value strictly greater than <b>K</b>.

<b>Example 1:</b>

<pre><b>Input:
</b>N = 3, K = 2
Arr[] = {3, 2, 1}
<b>Output:</b> 3
<b>Explanation:</b> The subarrays having value
strictly greater than K are: [3], [3, 2]
and [3, 2, 1]. Thus there are 3 such
subarrays.
</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N = 4, K = 1
Arr[] = {1, 2, 3, 4}
<b>Output:</b> 9
<b>Explanation:</b> There are 9 subarrays having
value strictly greater than K.
</pre>

<b>Your Task:</b><br>
Complete the function <b>countSubarray()</b> which takes an array <b>arr,</b> two integers <b>n, k,</b> as input parameters and returns an integer denoting the answer. You don't to print answer or take inputs.

<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Auxiliary Space:</b> O(1)<br>
<br>
<b>Constraints:</b><br>
1 <= N <= 10<sup>5</sup><br>
1 <= Arr[i] <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Dynamic Programming` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Count Subarrays Whose Maximum Element Greater K](https://www.geeksforgeeks.org/count-subarrays-whose-maximum-element-greater-k/)
