<h1 align="center">Largest Sum Subarray of Size at least K</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 37.64%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 60K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>a</b> of length <b>n </b>and a number <b>k</b>, find the <b>largest sum </b>of the [<b>subarray</b>](https://www.geeksforgeeks.org/array-subarray-subsequence-and-subset/) containing <b>at least k </b>numbers. It is guaranteed that the size of array is <b>at-least k</b>.

<b>Example 1:</b>

<pre><b>Input : 
</b>n = 4
a[] = {1, -2, 2, -3}
k = 2
<b>Output : </b>
1
<b>Explanation :</b>
The sub-array of length at-least 2<br>that produces greatest sum is {1, -2, 2}</pre>

<b>Example 2:</b>
<pre><b>Input :
</b>n = 6<b> </b>
a[] = {1, 1, 1, 1, 1, 1}
k = 2
<b>Output : </b>
6<br><b>Explanation :<br></b>The sub-array of length at-least 2<br>that produces greatest sum is {1, 1, 1, 1, 1, 1}</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>maxSumWithK()</b> which takes the array <b>a[]</b>, its size <b>n </b>and an integer <b>k </b>as inputs and returns the value of the <b>largest sum </b>of the subarray containing <b>at least k </b>numbers.

<b>Expected Time Complexity:</b> O(n)<br><b>Expected Auxiliary Space:</b> O(n)

<b>Constraints:</b><br>1 <= n <= 10<sup>5</sup><br>-10<sup>5 </sup><= a[i] <= 10<sup>5</sup><br>1 <= k <= n


<hr>

### Tags
- **Topic Tags:** `sliding-window` `Arrays` `Dynamic Programming` `Data Structures` `Algorithms`
- **Company Tags:** `Facebook` `Paytm` `Myntra`

### Related Articles
- [Largest Sum Subarray Least K Numbers](https://www.geeksforgeeks.org/largest-sum-subarray-least-k-numbers/)
