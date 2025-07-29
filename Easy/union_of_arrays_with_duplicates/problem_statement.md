<h1 align="center">Union of Arrays with Duplicates</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 42.22%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 450K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 10m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given two arrays <b>a[]</b> and <b>b[]</b>, return the <b>Union</b> of both the arrays in any order.

The <b>Union</b> of two arrays is a collection of all <b>distinct elements</b> present in either of the arrays. If an element appears more than once in one or both arrays, it should be included <b>only once </b>in the result.

<b>Note: </b>Elements of <b>a[] </b>and <b>b[]</b> are not necessarily distinct.<br>Note that, You can return the Union in any order but the driver code will print the result in <b>sorted order </b>only.

<b>Examples:</b>

<pre><b>Input:</b> a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
<b>Output: </b>[1, 2, 3]<b>
Explanation: </b>Union set of both the arrays will be 1, 2 and 3.
</pre>

<pre><b>Input: </b>a[] =<b> </b>[1, 2, 3], b[] = [4, 5, 6] <br><b>Output: </b>[1, 2, 3, 4, 5, 6]<b>
Explanation: </b>Union set of both the arrays will be 1, 2, 3, 4, 5 and 6.</pre>

<pre><b>Input: </b>a[] =<b> </b>[1, 2, 1, 1, 2], b[] = [2, 2, 1, 2, 1] <br><b>Output: </b>[1, 2]<b>
Explanation: </b>Union set of both the arrays will be 1 and 2.</pre>

<b>Constraints:</b><br>1 ≤ a.size(), b.size() ≤ 10<sup>6<br></sup>0 ≤ a[i], b[i] ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n + m)
- Auxiliary Space: O(n + m)

<hr>

### Tags
- **Topic Tags:** `Hash` `Data Structures` `Algorithms` `Arrays`
- **Company Tags:** `Zoho` `Rockstand`

### Related Articles
- [Union Of Two Arrays](https://www.geeksforgeeks.org/Union of Two Arrays/)
