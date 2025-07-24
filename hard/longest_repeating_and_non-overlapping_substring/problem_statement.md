<h1 align="center">Longest repeating and non-overlapping substring</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 46.71%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 45K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>s</b>, find the longest repeating non-overlapping substring in it. In other words find 2 identical substrings of maximum length which <b>do not overlap</b>. Return the longest non-overlapping substring. Return <b>-1</b> if no such string exists.

Note:<b> </b>Multiple Answers are possible but you have to return the substring whose <b>first occurrence</b> is earlier.

For Example: "abhihiab", here both <b>"ab"</b> and <b>"hi"</b> are possible answers. But you will have to return <b>"ab"</b> because its first occurrence appears before the first occurrence of "hi".

<b>Examples:</b>

<pre><b>Input:</b> s =<b> </b>"acdcdacdc"
<b>Output: </b>"acdc"
<b>Explanation: </b>The string "acdc" is the longest Substring of s which is repeating but not overlapping.</pre>

<pre><b>Input:</b> s = "geeksforgeeks"<br><b>Output: </b>"geeks"<br><b>Explanation: </b>The string "geeks" is the longest subString of s which is repeating but not overlapping.<br></pre>

<pre><b>Input:</b> s =<b> </b>"heheheh"
<b>Output: </b>"heh"
<b>Explanation: </b>The string "heh" is the longest Substring of s which is repeating but not overlapping.</pre>

<b>Constraints:</b><br>1 <= s.size() <= 10<sup>3</sup><br>s contains only lowercase English alphabets.

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(n^2)

<hr>

### Tags
- **Topic Tags:** `Strings` `Dynamic Programming` `Data Structures` `Algorithms`
- **Company Tags:** `MakeMyTrip` `Walmart`

### Related Articles
- [Longest Repeating And Non Overlapping Substring](https://www.geeksforgeeks.org/longest-repeating-and-non-overlapping-substring/)

### Related Interview Experiences
- [Makemytrip Interview Experience For Software Engineer](https://www.geeksforgeeks.org/makemytrip-interview-experience-for-software-engineer/)
