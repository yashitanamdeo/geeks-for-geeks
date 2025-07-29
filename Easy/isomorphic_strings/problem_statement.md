<h1 align="center">Isomorphic Strings</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 34.21%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 204K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings <b>s1</b> and <b>s2 </b>consisting of only lowercase English letters and of <b>equal length</b>, check if these two strings are <b>isomorphic </b>to each other.<br>If the characters in s1 can be changed to get s2, then two strings, s1 and s2 are isomorphic. A character must be completely swapped out for another character while maintaining the order of the characters. A character may map to itself, but no two characters may map to the same character.

<b>Examples:</b>

<pre><b>Input: </b>s1 = "aab", s2 = "xxy"
<b>Output: </b>true<b>
Explanation: </b>Each character in s1 can be consistently mapped to a unique character in s2 (a → x, b → y).
</pre>

<pre><b>Input: </b>s1 = "aab", s2 = "xyz"
<b>Output: </b>false<b>
Explanation: </b>Same character 'a' in s1 maps to two different characters 'x' and 'y' in s2.</pre>

<pre><b>Input: </b>s1 = "abc", s2 = "xxz"
<b>Output: </b>false<b>
Explanation: </b>Two different characters 'a' and 'b' in s1 maps with same character 'x' in s2. </pre>

<b>Constraints:</b><br>1 ≤ s1.size() = s2.size() ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Strings` `Data Structures` `Hash`
- **Company Tags:** `Google`

### Related Articles
- [Check If Two Given Strings Are Isomorphic To Each Other](https://www.geeksforgeeks.org/check-if-two-given-strings-are-isomorphic-to-each-other/)
