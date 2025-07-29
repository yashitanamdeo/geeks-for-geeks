<h1 align="center">Minimize the Heights II</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 15.06%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 728K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 25m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b> denoting heights of <b>n</b> towers and a positive integer <b>k. </b>

For <b>each </b>tower, you must perform <b>exactly one</b> of the following operations <b>exactly once</b>.

- <b>Increase </b>the height of the tower by <b>k</b>
- <b>Decrease </b>the height of the tower by <b>k</b>
Find out the <b>minimum </b>possible difference between the height of the shortest and tallest towers after you have modified each tower.

You can find a slight modification of the problem [here](https://practice.geeksforgeeks.org/problems/minimize-the-heights-i/1/).<br><b>Note:</b> It is <b>compulsory </b>to increase or decrease the height by k for each tower.<b> </b>After the operation, the resultant array should <b>not</b> contain any <b>negative integers</b>.

<b>Examples :</b>

<pre><b>Input: </b>k = 2, arr[] = [1, 5, 8, 10]
<b>Output: </b>5
<b>Explanation: </b>The array can be modified as [1+k, 5-k, 8-k, 10-k] = [3, 3, 6, 8].The difference between the largest and the smallest is 8-3 = 5.
</pre>

<pre><b>Input: </b>k = 3, arr[] = [3, 9, 12, 16, 20]
<b>Output: </b>11
<b>Explanation: </b>The array can be modified as [3+k, 9+k, 12-k, 16-k, 20-k] -> [6, 12, 9, 13, 17].The difference between the largest and the smallest is 17-6 = 11. 
</pre>

<b>Constraints</b><br>1 ≤ k ≤ 10<sup>7</sup><br>1 ≤ n ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>7</sup>

## Expected Complexities
- Time Complexity: O(n log n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Greedy`
- **Company Tags:** `Microsoft` `Adobe`

### Related Articles
- [Minimize The Maximum Difference Between The Heights](https://www.geeksforgeeks.org/minimize-the-maximum-difference-between-the-heights/)
