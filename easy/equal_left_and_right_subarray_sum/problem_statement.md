<h1 align="center">Equal Left and Right Subarray Sum</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 55.07%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 36K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr</b>. The task is to find the <b>first index</b> in the array such that the sum of elements before it is equal to the sum of elements after it. Return -1 if no such point exists.

<b>Examples :</b>

<pre><b>Input: </b>arr[] = [1,3,5,2,2] 
<b>Output: </b>2<b> 
Explanation: </b>For second test case at position 2 elements before it (1+3) = elements after it (2+2).<b> </b>
</pre>

<pre><b>Input: </b>arr[] = [1]
<b>Output: </b>0<b>
Explanation: </b>Since its the only element hence it is the only point.<br></pre>

<pre><b>Input: </b>arr[] = [5, 4, 3, 2, 1]
<b>Output: -</b>1</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>6<br></sup>0 ≤ arr[i] ≤ 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `prefix-sum` `Arrays` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon` `Adobe`

### Related Articles
- [Find Element Array Sum Left Array Equal Sum Right Array](https://www.geeksforgeeks.org/find-element-array-sum-left-array-equal-sum-right-array/)
