<h1 align="center">Maximum sum of increasing order elements from n arrays</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.74%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 10K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given <b>n</b> arrays of size <b>m </b>each. Find maximum sum obtained by selecting a number from each array such that the element selected from the <b>i-th</b> array is more than the element selected from <b>(i-1)-th</b> array. If maximum sum cannot be obtained then return <b>0</b>.

<b>Example 1:</b>

<pre><b>â€‹Input :</b> arr[ ] = {{1,7,4,3}, {4,2,5,1}, {9,5,1,8}}
<b>Output :</b> 18
<b>Explanation:</b>
We can select 4 from the first array,
5 from second array and 9 from the third array.
</pre>

<br>
<b>â€‹Example 2:</b>

<pre><b>Input :</b> arr[ ] = {{9,8,7}, {6,5,4}, {3,2,1}} <b>
Output :</b>  0

</pre>

<b>Your Task:</b><br>
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <b>maximumSum()</b> that takes number of row <b>N</b>, a number of Column<b> M</b>, 2-d array <b>(arr)</b>, and return the maximum sum if cannot be obtained then return <b>0</b>. The driver code takes care of the printing.

<b>Expected Time Complexity:</b> O(N*M).<br>
<b>Expected Auxiliary Space:</b> O(1).

 

<b>Constraints:</b><br>
1 ≤ N, M ≤ 500


<hr>

### Tags
- **Topic Tags:** `Arrays` `Searching` `Greedy` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Maximum Sum Increasing Order Elements N Arrays](https://www.geeksforgeeks.org/maximum-sum-increasing-order-elements-n-arrays/)
