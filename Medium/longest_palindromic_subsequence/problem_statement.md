<h1 align="center">Longest Palindromic Subsequence</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 56.57%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 110K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>s</b>, return the <b>length </b>of the longest palindromic subsequence.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements.

A palindromic sequence is a sequence that reads the same forward and backward.

<b>Examples:</b>

<pre><b>Input: </b>s = "bbabcbcab"
<b>Output:</b> 7
<b>Explanation</b>: Subsequence "babcbab" is the longest subsequence which is also a palindrome.
</pre>

<pre><b>Input</b>: s = "abcd"
<b>Output:</b> 1
<b>Explanation</b>: "a", "b", "c" and "d" are palindromic and all have a length 1.
</pre>

<pre><b>Input</b>: s = "agbdba"
<b>Output:</b> 5
<b>Explanation</b>: The longest palindromic subsequence is "abdba", which has a length of 5. The characters in this subsequence are taken from the original string "agbdba", and they maintain the order of the string while forming a palindrome.</pre>

<b>Constraints:</b><br>1 ≤ s.size() ≤ 1000<br>The string contains only lowercase letters.

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(n^2)

<hr>

### Tags
- **Topic Tags:** `Strings` `Dynamic Programming` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon` `Google`

### Related Articles
- [Longest Palindromic Subsequence Dp 12](https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/)
