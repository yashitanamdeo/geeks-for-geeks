<h1 align="center">4 Sum - All Quadruples</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 19.94%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 207K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b> of integers and another integer <b>target</b>. Find all <b>unique </b>quadruples from the given array that sums up to <b>target</b>.

<b>Note:</b> All the quadruples should be internally sorted, ie for any quadruple [q1, q2, q3, q4] it should be : q1 <= q2 <= q3 <= q4.

<b>Examples :</b>

<pre><b>Input: </b>arr[] = [0, 0, 2, 1, 1], target = 3<br><b>Output:</b> [0, 0, 1, 2] <b>
Explanation: </b>Sum of 0, 0, 1, 2 is equal to 3.
</pre>

<pre><b>Input: </b>arr[] = [10, 2, 3, 4, 5, 7, 8], target = 23
<b>Output: </b>[[2, 3, 8, 10], [2, 4, 7, 10], [3, 5, 7, 8]] <b>
Explanation: </b>Sum of 2, 3, 8, 10 is 23, sum of 2, 4, 7, 10 is 23 and sum of 3, 5, 7, 8 is also 23.</pre>

<pre><b>Input: </b>arr[] = [0, 0, 2, 1, 1], target = 2<br><b>Output:</b> [0, 0, 1, 1] <b>
Explanation: </b>Sum of 0, 0, 1, 1 is equal to 2.</pre>

<b>Constraints:</b><br>1 <= arr.size() <= 200<br>-10<sup>6</sup> <= target <= 10<sup>6</sup><br>-10<sup>6</sup> <= arr[i] <= 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n^3)
- Auxiliary Space: O(n^2)

<hr>

### Tags
- **Topic Tags:** `Hash` `Sorting` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon` `Microsoft` `OYO Rooms` `Adobe` `Google`

### Related Articles
- [Find Four Elements That Sum To A Given Value Set 2](https://www.geeksforgeeks.org/find-four-elements-that-sum-to-a-given-value-set-2/)
