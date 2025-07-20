<h1 align="center">Perfect Sum Problem</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 20.58%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 545K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr</b> of non-negative integers and an integer <b>target</b>, the task is to count all subsets of the array whose sum is equal to the given target.

<b>Examples:</b>

<pre><b>Input</b>: arr[] = [5, 2, 3, 10, 6, 8], target = 10
<b>Output: </b>3
<b>Explanation</b>: The subsets {5, 2, 3}, {2, 8}, and {10} sum up to the target 10.</pre>

<pre><b>Input</b>: arr[] = [2, 5, 1, 4, 3], target = 10
<b>Output:</b> 3
<b>Explanation</b>: The subsets {2, 1, 4, 3}, {5, 1, 4}, and {2, 5, 3} sum up to the target 10.</pre>

<pre><b>Input</b>: arr[] = [5, 7, 8], target = 3<br><b>Output:</b> 0
<b>Explanation</b>: There are no subsets of the array that sum up to the target 3.</pre>

<pre><b>Input</b>: arr[] = [35, 2, 8, 22], target = 0<br><b>Output:</b> 1
<b>Explanation</b>: The empty subset is the only subset with a sum of 0.</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>3<br></sup>0 ≤ arr[i] ≤ 10<sup>3</sup><br>0 ≤ target ≤ 10<sup>3</sup><br>

## Expected Complexities
- Time Complexity: O(n*target)
- Auxiliary Space: O(n*target)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Amazon` `Microsoft` `Tesco`

### Related Articles
- [Count Of Subsets With Sum Equal To X Using Recursion](https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x-using-recursion/)
- [Count Of Subsets With Sum Equal To X](https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x/)
