<h1 align="center">Search Pattern (KMP-Algorithm)</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 45.04%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 121K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings, one is a text string <b>txt</b> and the other is a pattern string <b>pat</b>. The task is to print the <b>indexes</b> of <b>all the occurrences</b> of the pattern string in the text string. Use<b> 0-based</b> indexing while returning the indices.<br><b>Note: </b>Return an empty list in case of no occurrences of pattern.<br>

<b>Examples :</b>

<pre><b>Input: </b>txt = "abcab", pat = "ab"
<b>Output:</b> [0, 3]
<b>Explanation</b>: The string "ab" occurs twice in txt, one starts at index 0 and the other at index 3. 
</pre>

<pre><b>Input</b>: txt = "abesdu", pat = "edu"
<b>Output:</b> []
<b>Explanation</b>: There's no substring "edu" present in txt.<br></pre>

<pre><b>Input</b>: txt = "aabaacaadaabaaba", pat = "aaba"
<b>Output:</b> [0, 9, 12]
<b>Explanation</b>:<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/703119/Web/Other/blobid0_1731391225.png" alt="" title="" width="377" height="188"/><br></pre>

<b>Constraints:</b><br>1 ≤ txt.size() ≤ 10<sup>6</sup><br>1 ≤ pat.size() < txt.size()<br>Both the strings consist of lowercase English alphabets.

## Expected Complexities
- Time Complexity: O(n + m)
- Auxiliary Space: O(m)

<hr>

### Tags
- **Topic Tags:** `Strings` `Pattern Searching` `Data Structures` `Algorithms`
- **Company Tags:** `Microsoft`

### Related Articles
- [Kmp Algorithm For Pattern Searching](https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/)
