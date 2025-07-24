<h1 align="center">Search insert position of K in a sorted array</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 38.99%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 81K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a sorted array <b>Arr[]</b>(0-index based) consisting of <b>N </b>distinct integers and an integer <b>k</b>, the task is to find the index of k, if its present in the array <b>Arr[]</b>. Otherwise, find the index where <b>k</b> must be inserted to keep the array sorted.

<br>
<b>Example 1:</b>

<pre><b>Input:</b>
N = 4
Arr = {1, 3, 5, 6}
k = 5
<b>Output:</b> 2
<b>Explaination:</b> Since 5 is found at index 2 
as Arr[2] = 5, the output is 2.</pre>

<br>
<b>Example 2:</b>

<pre><b>Input:</b>
N = 4
Arr = {1, 3, 5, 6}
k = 2
<b>Output:</b> 1
<b>Explaination:</b> Since 2 is not present in 
the array but can be inserted at index 1 
to make the array sorted.
</pre>

<br>
<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>searchInsertK()</b> which takes the array <b>Arr[]</b> and its size <b>N </b>and <b>k </b>as input parameters and returns the index.

<br>
<b>Expected Time Complexity:</b> O(logN)<br>
<b>Expected Auxiliary Space:</b> O(1)

<br>
<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>4</sup><br>
-10<sup>3</sup> ≤ Arr[i] ≤ 10<sup>3</sup><br>
-10<sup>3</sup> ≤ k ≤ 10<sup>3</sup>


<hr>

### Tags
- **Topic Tags:** `Searching` `Algorithms`
- **Company Tags:** `Microsoft`

### Related Articles
- [Search Insert Position Of K In A Sorted Array](https://www.geeksforgeeks.org/search-insert-position-of-k-in-a-sorted-array/)
