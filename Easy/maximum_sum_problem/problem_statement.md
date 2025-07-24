<h1 align="center">Maximum Sum Problem</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 57.09%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 59K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

A number <b>n </b>can be broken into three parts<b> n/2</b>,<b> n/3</b>,<b> </b>and<b> n/4 </b>(consider only the <b>integer </b>part). Each number obtained in this process can be divided further recursively. Find the <b>maximum sum </b>that can be obtained by summing up the divided parts together.<br><b>Note: </b>It is possible that we don't divide the number at all.

<b>Example 1:</b>

<pre><b>Input:</b>
n = 12
<b>Output:</b> <br>13
<b>Explanation</b>: <br>Break n = 12 in three parts {12/2, 12/3, 12/4} = {6, 4, 3}, now current sum is = (6 + 4 + 3) = 13. Further breaking 6, 4 and 3 into parts will produce sum less than or equal to 6, 4 and 3 respectively.
</pre>

<b>Example 2:</b>

<pre><b>Input</b>:
n = 24
<b>Output:</b> <br>27
<b>Explanation</b>: <br>Break n = 24 in three parts {24/2, 24/3, 24/4} = {12, 8, 6}, now current sum is = (12 + 8 + 6) = 26 . But recursively breaking 12 would produce value 13. So our maximum sum is 13 + 8 + 6 = 27.
</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>maxSum() </b>which accepts an integer n and returns the maximum sum.<br>

<b>Expected Time Complexity: </b>O(n)<br><b>Expected Auxiliary Space: </b>O(n)

<b>Constraints:</b><br>0 <= n <= 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Morgan Stanley`

### Related Articles
- [Recursively Break Number 3 Parts Get Maximum Sum](https://www.geeksforgeeks.org/recursively-break-number-3-parts-get-maximum-sum/)
