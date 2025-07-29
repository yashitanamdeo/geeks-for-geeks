<h1 align="center">Recursively Remove Adjacent Duplicates</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 14.88%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 186K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string s, remove all its adjacent duplicate characters recursively, until there are no adjacent duplicate characters left.

Note: If the resultant string becomes empty, return an empty string.

<b>Examples:</b>

<pre><b>Input: </b>s = "geeksforgeek"
<b>Output:</b> "gksforgk"
<b>Explanation:  </b>g(ee)ksforg(ee)k -> gksforgk</pre>

<pre><b>Input: </b>s = "abccbccba"
<b>Output:</b> ""
<b>Explanation: </b>ab(cc)b(cc)ba->abbba->a(bbb)a->aa->(aa)->""(empty string)<br></pre>

<pre><b>Input: </b>s = "abcd"
<b>Output:</b> "abcd"
<b>Explanation: </b>There are no adjacent duplicate characters</pre>

<b>Constraints:</b><br>1<= s.size() <= 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Strings` `Recursion` `Data Structures` `Algorithms`
- **Company Tags:** `Paytm` `Samsung`

### Related Articles
- [Recursively Remove Adjacent Duplicates Given String](https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/)

### Related Interview Experiences
- [Paytm Interview Experience Set 15](https://www.geeksforgeeks.org/paytm-interview-experience-set-15/)
