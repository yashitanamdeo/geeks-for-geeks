<h1 align="center">Min Add to Make Parentheses Valid</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 57.97%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 12K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a string <b>s</b> consisting only of the characters <b>'('</b> and <b>')'</b>. Your task is to determine the <b>minimum</b> number of parentheses (either '(' or ')') that must be inserted at any positions to make the string s a <b>valid parentheses string</b>.

A parentheses string is considered <b>valid </b>if:<br>

1. Every opening parenthesis '(' has a corresponding closing parenthesis ')'.
1. Every closing parenthesis ')' has a corresponding opening parenthesis '('.
1. Parentheses are properly nested.
<b>Examples:</b>

<pre><b>Input: </b>s = "(()("
<b>Output:</b> 2
<b>Explanation:</b> There are two unmatched '(' at the end, so we need to add two ')' to make the string valid.</pre>

<pre><b>Input: </b>s = ")))"
<b>Output:</b> 3
<b>Explanation: </b>Three '(' need to be added at the start to make the string valid.</pre>

<pre><b>Input: </b>s = ")()()"
<b>Output:</b> 1 <br><b>Explanation: </b>The very first ')' is unmatched, so we need to add one '(' at the beginning.</pre>

<b>Constraints:</b><br>1 ≤ s.size() ≤ 10<sup>5</sup><br>s[i] ∈ { '(' , ')' }

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Stack` `Strings` `Data Structures`
- **Company Tags:** `Amazon` `Microsoft` `TCS` `Adobe` `IBM`

### Related Articles
- [Minimum Number Of Parentheses To Be Added To Make It Valid](https://www.geeksforgeeks.org/minimum-number-of-parentheses-to-be-added-to-make-it-valid/)
