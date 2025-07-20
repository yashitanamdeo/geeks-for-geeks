<h1 align="center">Search Pattern (Rabin-Karp Algorithm)</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 34.53%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 87K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings:

- 
A <b>text</b> string in which you want to search.


- 
A <b>pattern</b> string that you are looking for within the <b>text</b>.


Return all <b>positions </b>(1-based indexing) where the <b>pattern</b> occurs as a substring in the <b>text</b>. 

<b>Note:</b> If the pattern does not occur in text, return an empty list.

<b>Examples:</b>

<pre><b>Input</b>: text = "birthdayboy", pattern = "birth"<br><b>Output:</b> [1]
<b>Explanation</b>: The string "birth" occurs at index 1 in text.</pre>

<pre><b>Input: </b>text = "geeksforgeeks", pattern = "geek"
<b>Output:</b> [1, 9]
<b>Explanation</b>: The string "geek" occurs twice in text, one starts at index 1 and the other at index 9.</pre>

<b>Constraints:</b><br>1 ≤ text.size() ≤ 10<sup>6</sup><br>1 ≤ pattern.size() ≤ text.size()<br>Both the strings consist of lowercase english alphabets.

## Expected Complexities
- Time Complexity: O(n + m)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Strings` `Pattern Searching` `Data Structures` `Algorithms`
- **Company Tags:** `Microsoft`

### Related Articles
- [Rabin Karp Algorithm For Pattern Searching](https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/)
