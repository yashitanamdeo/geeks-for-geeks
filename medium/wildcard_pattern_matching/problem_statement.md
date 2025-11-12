<h1 align="center">Wildcard Pattern Matching</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 31.13%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 94K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings <b><b>pat </b></b>and <b><b>txt</b></b> which may be of different sizes, You have to return <b><b>true</b></b> if the wildcard pattern i.e. <b><b>pat</b></b>,<b><b> </b></b>matches with <b><b>txt</b></b> else return <b><b>false</b></b>.

The wildcard pattern <b><b>pat</b></b> can include the characters '<b><b>?</b></b>' and '<b><b>*</b></b>'.

- '<b><b>?</b></b>' – matches any single character.
- '<b><b>*</b></b>' – matches any sequence of characters (including the empty sequence).
<b><b>Note: </b></b>The matching should cover the entire <b><b>txt</b></b> (not partial <b><b>txt</b></b>).

<b>Examples:</b>

<pre><b>Input:</b> txt = "abcde", pat = "a?c*"
<b>Output:</b> true
<b>Explanation: </b>'?' matches with 'b' and '*' matches with "de".
</pre>

<pre><b>Input:</b> txt = "baaabab", pat = "a*ab"
<b>Output:</b> false
<b>Explanation</b>: The pattern starts with a, but the text starts with b, so the pattern does not match the text.</pre>

<pre><b>Input</b>: txt = "abc", pat = "*"
<b>Output:</b> true
<b>Explanation</b>: '*' matches with whole text "abc".</pre>

<b>Constraints:</b><br>1 ≤ txt.size(), pat.size() ≤ 100

## Expected Complexities
- Time Complexity: O(n * m)
- Auxiliary Space: O(n * m)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms` `Recursion` `Strings`
- **Company Tags:** `Zoho` `Amazon` `Microsoft` `Ola Cabs` `Walmart` `Google` `InMobi` `United Health Group`

### Related Articles
- [Wildcard Pattern Matching](https://www.geeksforgeeks.org/wildcard-pattern-matching/)

### Related Interview Experiences
- [Walmart Lab Interview Experience Set 9 Off Campus](https://www.geeksforgeeks.org/walmart-lab-interview-experience-set-9-off-campus/)
