<h1 align="center">Unique partitions</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 63.11%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 14K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a positive integer <b>n</b>, generate all possible unique ways to represent <b>n</b> as sum of positive integers.

<b>Note: </b>The generated output is printed without partitions. Each partition must be in decreasing order. Printing of all the partitions is done in reverse sorted order. <br><br><b>Example 1:</b>

<pre><b>Input: </b>n = 3
<b>Output: </b>3 2 1 1 1 1
<b>Explanation: </b>For n = 3, 
{3}, {2, 1} and {1, 1, 1}.
</pre>

 

<b>Example 2:</b>

<pre><b>Input: </b>n = 4 
<b>Output: </b>4 3 1 2 2 2 1 1 1 1 1 1
<b>Explanation: </b>For n = 4, 
{4}, {3, 1}, {2, 2}, {2, 1, 1}, {1, 1, 1, 1}.
</pre>

<br><b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>UniquePartitions() </b>which takes n as input parameter and returns a list of all possible combinations in lexicographically decreasing order. <br> 

<b>Expected Time Complexity: </b>O(2<sup>n</sup>)<br><b>Expected Space Complexity: </b>O(2<sup>n</sup>)<br><br> 

<b>Constraints:</b><br>1 <= n <= 25


<hr>

### Tags
- **Topic Tags:** `Recursion` `Backtracking` `Algorithms`
- **Company Tags:** `Amazon`

### Related Articles
- [Generate Unique Partitions Of An Integer](https://www.geeksforgeeks.org/generate-unique-partitions-of-an-integer/)
