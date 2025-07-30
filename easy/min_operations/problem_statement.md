<h1 align="center">Min operations</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 57.82%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 20K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two numbers <b>a</b> and <b>b</b>. In one operation you can pick any non negative integer<b> x </b>and either of <b>a</b> or <b>b</b>. Now if you picked <b>a</b> then replace <b>a</b> with <b>a&x</b> else if you picked <b>b</b> then replace <b>b</b> with <b>b&x</b>.

Return the minimum number of operation required to make <b>a</b> and<b> b</b> equal.<br>
<br>
Note: Here <b>& </b>represents bitwise <b>AND</b> operation.

<b>Example 1:</b>

<pre><b>Input:
</b>a = 5, b = 12
<b>Output:</b>
2
<b>Explanantion:</b>
In first operation replace 
a = a&4 = 4
after that replace 
b = b&6 = 4
Hence both are same after applying two
operations.
</pre>

<b>Example 2:</b>

<pre><b>Input:</b> 
a = 100, b = 100
<b>Output:</b> 
0
<b>Explanation</b>: 
Already same.</pre>

<b>Your Task:</b><br>
You don't need to read, input, or print anything. Your task is to complete the function <b><i>solve( )</i>, </b>which takes two integers <b>a</b> and <b>b </b>as input parameters and returns the answer.

## Expected Time Complexity: O(1)<br>
Expected Auxiliary Space: O(1)
<b>Constraints:</b><br>
0 ≤ a, b ≤ 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `None`
- **Company Tags:** `None`
