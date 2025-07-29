<h1 align="center">Longest Substring with K Uniques</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 34.65%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 219K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a string <b>s</b> consisting only lowercase alphabets and an integer <b>k</b>. Your task is to find the <b>length </b>of the <b>longest substring</b> that contains exactly <b>k</b> distinct characters.

<b>Note :</b> If no such substring exists, return <b>-1</b>. 

<b>Examples:</b>

<pre><b>Input: </b>s = "aabacbebebe", k = 3
<b>Output:</b> 7
<b>Explanation</b>: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.
</pre>

<pre><b>Input</b>: s = "aaaa", k = 2
<b>Output:</b> -1
<b>Explanation</b>: There's no substring with 2 distinct characters.<br></pre>

<pre><b>Input: </b>s = "aabaaab", k = 2
<b>Output:</b> 7
<b>Explanation</b>: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.</pre>

<b>Constraints:</b><br>1 ≤ s.size() ≤ 10<sup>5</sup><br>1 ≤ k ≤ 26<br>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `two-pointer-algorithm` `Hash` `Strings` `Map` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon` `Google` `SAP Labs`

### Related Articles
- [Find The Longest Substring With K Unique Characters In A Given String](https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/)
