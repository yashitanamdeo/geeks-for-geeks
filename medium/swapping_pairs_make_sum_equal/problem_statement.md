<h1 align="center">Swapping pairs make sum equal</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 23.94%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 133K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two arrays of integers <b>a[]</b> and <b>b[]</b>, the task is to check if a pair of values (one value from each array) exists such that swapping the elements of the pair will make the sum of two arrays equal.

<b>Examples :</b>

<pre><b>Input: </b>a[] = [4, 1, 2, 1, 1, 2], b[] = [3, 6, 3, 3]
<b>Output: </b>true
<b>Explanation</b>: Sum of elements in a[] = 11, Sum of elements in b[] = 15, To get same sum from both arrays, we can swap following values: 1 from a[] and 3 from b[]</pre>

<pre><b>Input: </b>a[] = [5, 7, 4, 6], b[] = [1, 2, 3, 8]
<b>Output:</b> true
<b>Explanation</b>: We can swap 6 from array a[] and 2 from array b[]<br></pre>

<pre><b>Input: </b>a[] = [3, 3], b[] = [6, 5, 6, 6]
<b>Output:</b> false</pre>

<b>Constraints:</b><br>1 ≤ a.size() ≤ 10<sup>6<br></sup>1 ≤ b.size() ≤ 10<sup>6<br></sup>1 ≤ a[i] ≤ 10<sup>3<br></sup>1 ≤ b[i] ≤ 10<sup>3</sup>

## Expected Complexities
- Time Complexity: O(n * log n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Hash` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Find A Pair Swapping Which Makes Sum Of Two Arrays Same](https://www.geeksforgeeks.org/find-a-pair-swapping-which-makes-sum-of-two-arrays-same/)
