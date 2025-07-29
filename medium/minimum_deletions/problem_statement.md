<h1 align="center">Minimum Deletions</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 58.8%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 70K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>s</b>, write a program to delete the <b>minimum number </b>of characters from the string so that the resultant string is a <b>palindrome</b>, while maintaining the order of characters.

<b>Examples:</b>

<pre><b>Input: </b>s<b> </b>=<b> "</b>aebcbda"
<b>Output:</b> 2
<b>Explanation</b>: Remove characters 'e' and 'd'.</pre>

<pre><b>Input</b>: s = "geeksforgeeks"
<b>Output:</b> 8
<b>Explanation</b>: To make "geeksforgeeks" a palindrome, the longest palindromic subsequence is "eefee" (length 5). The minimum deletions are:<br>13 (length of s)<b> - </b>5 <b>= </b>8.</pre>

<b>Constraints:</b><br>1 ≤ s.size() ≤ 10<sup>3</sup>

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Strings` `Dynamic Programming` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon`

### Related Articles
- [Minimum Number Deletions Make String Palindrome](https://www.geeksforgeeks.org/minimum-number-deletions-make-string-palindrome/)
