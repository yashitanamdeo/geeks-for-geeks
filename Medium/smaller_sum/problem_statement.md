<h1 align="center">Smaller Sum</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.81%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 30K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array <b>arr</b> of <b>n</b> integers. For each index i, you have to find the sum of all integers present in the array with a value <b>less</b> than arr[i].

<b>Example 1:</b>

<pre><b>Input:</b>
n = 3
arr = {1, 2, 3}
<b>Output:</b>
0 1 3
<b>Explanation:</b>
For 1, there are no elements lesser than itself.
For 2, only 1 is lesser than 2.
And for 3, 1 and 2 are lesser than 3, so the sum is 3.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
n = 2
arr = {4, 4}
<b>Output:</b>
0 0
<b>Explanation:
</b>For 4, there are no elements lesser than itself. 
For 4, there are no elements lesser than itself.
There are no smaller elements than 4.</pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>smallerSum()</b> which takes an integer <b>n</b> and an array <b>arr</b> and returns an array of length <b>n</b> , the answer for every index.

<b>Expected Time Complexity</b>:O(n log n)<br>
<b>Expected Space Complexity</b>:O(n)<br>
<br>
<b>Constraints:</b><br>
1 <= n <= 10<sup>5</sup><br>
0 <= arr[i] <= 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Binary Search` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find The Sum Of All Values Lesser Than The Element Of The Array](https://www.geeksforgeeks.org/find-the-sum-of-all-values-lesser-than-the-element-of-the-array/)
