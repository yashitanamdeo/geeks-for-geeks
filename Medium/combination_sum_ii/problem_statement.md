<h1 align="center">Combination Sum II</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.5%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 43K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b> and a <b>target</b>, your task is to find all <b>unique </b>combinations in the array where the sum is equal to target. Each number in arr[] may only be used <b>once </b>in the combination.

You can return your answer in <b>any </b>order.

<b>Examples:</b>

<pre><b>Input:</b> arr[] = [1, 2, 3, 3, 5], target =7
<b>Output: </b>[[1, 3, 3], [2, 5]]
<b>Explanation: </b>Total number of possible combinations are 2.</pre>

<pre><b>Input: </b>arr[] = [5, 10, 15, 20, 25, 30], target = 30
<b>Output: </b>[[5, 10, 15], [5, 25], [10, 20], [30]]
<b>Explanation: </b>Total number of possible combinations are 4.<br></pre>

<pre><b>Input: </b>arr[] = [6, 5, 7], target = 8
<b>Output: </b>[]<br><b>Explanation:</b> There are no possible combinantions such that target sum is 8.</pre>

<b>Constraints:</b><br>1 <= arr.size() <= 100<br>1 <= arr[i] <= 50<br>1 <= target <= 30

## Expected Complexities
- Time Complexity: (2^n) * n
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Recursion` `Data Structures` `Algorithms` `Backtracking`
- **Company Tags:** `None`

### Related Articles
- [All Unique Combinations Whose Sum Equals To K](https://www.geeksforgeeks.org/all-unique-combinations-whose-sum-equals-to-k/)
