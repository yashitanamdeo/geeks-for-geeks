<h1 align="center">Check if a String is Subsequence of Other</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.68%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 33K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings <b>s1</b> and <b>s2</b>. You have to check that <b>s1</b> is a subsequence of <b>s2 </b> or not. <br><b>Note:</b> A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

<b>Examples:</b>

<pre><b>Input: </b>s1 = "AXY", s2 = "YADXCP"
<b>Output: </b>false
<b>Explanation:</b> s1 is not a subsequence of s2 as 'Y' appears before 'A'.</pre>

<pre><b>Input: </b>s1 = "gksrek", s2 = "geeksforgeeks"
<b>Output:</b> true
<b>Explanation: </b>If we combine the bold character of "<b>g</b>ee<b>ks</b>fo<b>r</b>g<b>e</b>e<b>k</b>s", it equals to s1. So s1 is a subsequence of s2. </pre>

<b>Constraints:</b><br>1 ≤ s1.size(), s2.size() ≤ 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Strings` `Greedy` `two-pointer-algorithm`
- **Company Tags:** `None`

### Related Articles
- [Given Two Strings Find First String Subsequence Second](https://www.geeksforgeeks.org/given-two-strings-find-first-string-subsequence-second/)
