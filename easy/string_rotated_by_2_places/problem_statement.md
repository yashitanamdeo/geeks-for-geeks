<h1 align="center">String Rotated by 2 Places</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 32.7%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 250K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings <b>s1 </b>and <b>s2</b>. Return true if the string <b>s2</b> can be obtained by rotating (<b>in any direction</b>) string <b>s1</b> by <b>exactly 2</b> places, otherwise, false.

<b>Note:</b> Both rotations should be performed in same direction chosen initially.

<b>Examples:</b>

<pre><b>Input: </b>s1 = "amazon", s2 = "azonam"
<b>Output: </b>true<b>
Explanation: "</b>amazon" can be rotated anti-clockwise by two places, which will make it as "azonam".
</pre>

<pre><b>Input: </b>s1 = "geeksforgeeks", s2 = "geeksgeeksfor"
<b>Output: </b>false<b>
Explanation: </b>If we rotate "geeksforgeeks" by two place in any direction, we won't get "geeksgeeksfor".<br></pre>

<pre><b>Input: </b>s1 = "ab", s2 = "ab"
<b>Output: </b>true<br><b>Explanation:</b> If we rotate "ab" by two place in any direction, we always get "ab".</pre>

<b>Challenge: </b>Try doing it in O(1) space complexity

<b>Constraints:</b><br>1 ≤ s1.length, s2.length ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Strings` `Data Structures`
- **Company Tags:** `Accolite` `Amazon`

### Related Articles
- [Check String Can Obtained Rotating Another String 2 Places](https://www.geeksforgeeks.org/check-string-can-obtained-rotating-another-string-2-places/)

### Related Interview Experiences
- [Accolite Interview Experience Set 5 On Campus](https://www.geeksforgeeks.org/accolite-interview-experience-set-5-on-campus/)
