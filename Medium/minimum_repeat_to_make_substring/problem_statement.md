<h1 align="center">Minimum repeat to make substring</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.22%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 68K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings <b>s1 </b>and<b> s2</b>.<b> </b>Return a <b>minimum</b> number of times s1 has to be <b>repeated </b>such that s2 is a <b>substring</b> of it. If s2 can never be a substring then return <b>-1</b>.

<b>Note:</b> Both the strings contain only lowercase letters.

<b>Examples:</b>

<pre><b>Input: </b>s1 = "ww", s2 = "www"
<b>Output: </b>2
<b>Explanation: </b>Repeating s1 two times "<b>www</b>w", s2 is a substring of it.</pre>

<pre><b>Input: </b>s1 = "abcd", s2 = "cdabcdab" <br><b>Output: </b>3 <br><b>Explanation: </b>Repeating s1 three times "ab<b>cdabcdab</b>cd", s2 is a substring of it. s2 is not a substring of s1 when it is repeated less than 3 times.</pre>

<pre><b>Input: </b>s1 = "ab", s2 = "cab"
<b>Output: </b>-1
<b>Explanation: </b>No matter how many times we repeat s1, we can't get a string such that s2 is a substring of it.</pre>

<b>Constraints:</b><br>1 ≤ s1.size(), s2.size() ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n + m)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Searching` `Strings` `Pattern Searching` `Data Structures` `Algorithms`
- **Company Tags:** `Google`

### Related Articles
- [Minimum Number Of Times A Has To Be Repeated Such That B Is A Substring Of It](https://www.geeksforgeeks.org/minimum-number-of-times-a-has-to-be-repeated-such-that-b-is-a-substring-of-it/)

### Related Interview Experiences
- [Google Interview Experience Set 7 Software Engineering Intern](https://www.geeksforgeeks.org/google-interview-experience-set-7-software-engineering-intern/?ref=rp)
