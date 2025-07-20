<h1 align="center">Find the longest string</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 56.04%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 37K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of strings <b>words</b><b>[]</b>. Find the <b>longest</b> string in words[] such that <b>every prefix</b> of it is also present in the array words[]. <br>

<b>Note: </b>If multiple strings have the same maximum length, return the <b>lexicographically smallest one</b>.

<b>Examples:</b>

<pre><b>Input:</b> words[] = ["p", "pr", "pro", "probl", "problem", "pros", "process", "processor"]
<b>Output:</b> pros
<b>Explanation: </b>"pros" is the longest word with all prefixes ("p", "pr", "pro", "pros") present in the array words[].</pre>

<pre><b>Input: </b>words[] = ["ab", "a", "abc", "abd"]
<b>Output: </b>abc
<b>Explanation:</b> Both "abc" and "abd" has all the prefixes in words[]. Since, "abc" is lexicographically smaller than "abd", so the output is "abc".
</pre>

<b>Constraints:</b><br>1 ≤ words.length() ≤ 10<sup>3</sup><br>1 ≤ words[i].length ≤ 10<sup>3</sup>

## Expected Complexities
- Time Complexity: O(n * max(words[i].size()) )
- Auxiliary Space: O(n * max(words[i].size()) )

<hr>

### Tags
- **Topic Tags:** `Strings` `BFS` `Trie` `Data Structures` `Algorithms` `Advanced Data Structure`
- **Company Tags:** `Flipkart`

### Related Articles
- [Longest Valid Word With All Prefixes](https://www.geeksforgeeks.org/longest-valid-word-with-all-prefixes/)

### Related Interview Experiences
- [Flipkart Interview Set 15 Sde Ii](https://www.geeksforgeeks.org/flipkart-interview-set-15-sde-ii/)
