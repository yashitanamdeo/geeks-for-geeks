<h1 align="center">Max of min for every window size</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 42.9%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 75K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 45m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an integer array <b>arr[]</b>, the task is to find the <b>maximum of minimum values</b> for every window size <b>k</b> where <b>1≤ k ≤ arr.size()</b>.

For each window size<b> k</b>, consider all contiguous subarrays of length <b>k</b>, determine the minimum element in each subarray, and then take the maximum among all these minimums.

Return the results as an array, where the element at index <b>i</b> represents the answer for window size <b>i+1</b>.

<b>Examples :</b>

<pre><b>Input: </b>arr[] = [10, 20, 30, 50, 10, 70, 30]
<b>Output: </b>[70, 30, 20, 10, 10, 10, 10] <b>
Explanation: <br></b>Window size 1: minimums are [10, 20, 30, 50, 10, 70, 30], maximum of minimums is 70.<br>Window size 2: minimums are [10, 20, 30, 10, 10, 30], maximum of minimums is 30.<br>Window size 3: minimums are [10, 20, 10, 10, 10], maximum of minimums is 20.<br>Window size 4–7: minimums are [10, 10, 10, 10], maximum of minimums is 10.</pre>

<pre><b>Input: </b>arr[] = [10, 20, 30]
<b>Output: </b>[30, 20, 10]<b>
Explanation: <br></b>Window size 1: minimums of  [10], [20], [30], maximum of minimums is 30.<br>Window size 2: minimums of [10, 20], [20,30], maximum of minimums is 20.<br>Window size 3: minimums of [10,20,30], maximum of minimums is 10.</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `sliding-window` `Stack` `Data Structures` `Algorithms`
- **Company Tags:** `Flipkart` `Amazon` `Microsoft`

### Related Articles
- [Find The Maximum Of Minimums For Every Window Size In A Given Array](https://www.geeksforgeeks.org/find-the-maximum-of-minimums-for-every-window-size-in-a-given-array/)

### Related Interview Experiences
- [Amazon Interview Experience Set 384 Campus Fte](https://www.geeksforgeeks.org/amazon-interview-experience-set-384-campus-fte/)
