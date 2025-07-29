<h1 align="center">Max min Height</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 62.86%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 30K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a garden with <b>n</b> flowers planted in a row, that is represented by an array <b>arr[]</b>, where arr[i] denotes the<b> </b>height of the i<sup>th</sup> flower.You will water them for <b>k</b> days. In one day you can water <b>w</b> continuous flowers. Whenever you water a flower its <b>height</b> increases by <b>1</b> unit. You have to <b>maximize</b> the <b>minimum </b>height of all flowers after  <b>k</b> days of watering.

<b>Examples:</b>

<pre><b>Input:</b> arr[] = [2, 3, 4, 5, 1], k = 2, w = 2
<b>Output:</b> 2
<b>Explanation:</b> The minimum height after watering is 2.<br>Day 1: Water the last two flowers -> arr becomes [2, 3, 4, 6, 2]
Day 2: Water the last two flowers -> arr becomes [2, 3, 4, 7, 3]</pre>

<pre><b>Input: </b>arr[] = [5, 8], k = 5, w = 1
<b>Output: </b>9
<b>Explanation: </b>The minimum height after watering is 9.<br>Day 1 - Day 4: Water the first flower -> arr becomes [9, 8]
Day 5: Water the second flower -> arr becomes [9, 9]</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>5</sup><br>1 ≤ w ≤ arr.size()<br>1 ≤ k ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>9</sup>

## Expected Complexities
- Time Complexity: O(n log m)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Dynamic Programming` `Binary Search` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Maximizing Smallest Flower Height In Garden With Watering Constraint](https://www.geeksforgeeks.org/maximizing-smallest-flower-height-in-garden-with-watering-constraint/)
