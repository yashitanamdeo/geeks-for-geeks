<h1 align="center">Distinct occurrences</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 27.37%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 72K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given two strings <b>txt</b> and <b>pat</b>, find the count of <b>distinct </b>occurrences of <b>pat</b> as a subsequence in <b>txt</b>.

<b>Note:</b> It is guaranteed that the ans will fit within a 32-bit integer.

<b>Examples:</b>

<pre><b>Input: </b>txt = "abba", pat = "aba"
<b>Output:</b> 2
<b>Explanation</b>: There are 2 sub-sequences: [abba], [abba].</pre>

<pre><b>Input</b>: txt = "banana", pat = "ban"
<b>Output:</b> 3
<b>Explanation</b>: There are 3 sub-sequences: [banana], [banana], [banana].
</pre>

<b>Constraints:</b><br>1 ≤ txt.size() ≤ pat.size() ≤ 10<sup>3</sup><br>Both txt and pat contain only lowercase alphabets.

## Expected Complexities
- Time Complexity: O(n * m)
- Auxiliary Space: O(n * m)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Amazon` `Google`

### Related Articles
- [Count Distinct Occurrences As A Subsequence](https://www.geeksforgeeks.org/count-distinct-occurrences-as-a-subsequence/)
