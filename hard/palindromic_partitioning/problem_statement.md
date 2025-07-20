<h1 align="center">Palindromic Partitioning</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 27.82%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 158K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>s</b>, a partitioning of the string is a<b> palindrome partitioning </b>if every sub-string of the partition is a <b>palindrome</b>. Determine the <b>fewest cuts</b> needed for <b>palindrome partitioning</b> of the given string.

<b>Examples:</b>

<pre><b><b>Input:</b></b> s = "geek" <br><b><b>Output:</b></b> 2 <br><b><b>Explanation: </b></b>We need to make minimum 2 cuts, i.e., "g | ee | k".</pre>

<pre><b><b>Input: </b></b>s = "aaaa" <br><b><b>Output</b></b>: 0<br><b><b>Explanation:</b></b> The string is already a palindrome.</pre>

<pre><b>Input:</b> s = "ababbbabbababa" <br><b>Output: </b>3<br><b>Explanation:</b> We need to make minimum 3 cuts, i.e., "aba | bb | babbab | aba".</pre>

<b>Constraints:</b><br>1 ≤ |s| ≤ 10<sup>3<br></sup><sup>s contain lowercase letters only</sup>

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(n^2)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Amazon` `Microsoft` `Google`

### Related Articles
- [Palindrome Partitioning Dp 17](https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/)
