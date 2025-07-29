<h1 align="center">Maximum Sum Combination</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.69%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 98K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given two integer arrays <b>a[]</b> and <b>b[]</b> of equal size. A sum combination is formed by adding one element from <b>a[]</b> and one from <b>b[]</b>, using each index pair <b>(i, j)</b> at most once. Return the top<b> k maximum </b>sum combinations, sorted in non-increasing order.

<b>Examples:</b>

<pre><b>Input: </b>a[] = [3, 2], b[] = [1, 4], k = 2<b><br>Output: </b>[7, 6]<b><br>Explanation: </b>Possible sums: 3 + 1 = 4, 3 + 4 = 7, 2 + 1 = 3, 2 + 4 = 6, Top 2 sums are 7 and 6.<br></pre>

<pre><b>Input: </b>a[] = [1, 4, 2, 3], b[] = [2, 5, 1, 6], k = 3<b><br></b><b>Output:</b> [10, 9, 9]<br><b>Explanation:</b><b> </b>The top 3 maximum possible sums are : 4 + 6 = 10, 3 + 6 = 9, and 4 + 5 = 9<br></pre>

<b>Constraints:<br></b>1 ≤ a.size() = b.size() ≤ 10<sup>5</sup><br>1 ≤ k ≤ a.size()<br>1 ≤ a[i], b[i] ≤ 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n log n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Sorting` `Heap` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [K Maximum Sum Combinations Two Arrays](https://www.geeksforgeeks.org/k-maximum-sum-combinations-two-arrays/)
