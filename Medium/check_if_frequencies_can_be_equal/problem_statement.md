<h1 align="center">Check if frequencies can be equal</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 16.67%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 142K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>s</b> consisting only lowercase alphabetic characters, check whether it is possible to remove <b>at most one character</b> such that the  frequency of each distinct character in the string becomes same. Return <b>true</b> if it is possible; otherwise, return <b>false</b>.<br>

<b>Examples:<br></b>

<pre><b>Input: </b>s = "xyyz"
<b>Output:</b> true 
<b>Explanation:</b> Removing one 'y' will make frequency of each distinct character to be 1.<br></pre>

<pre><b>Input: </b>s = "xyyzz"<br><b>Output: </b>true
<b>Explanation:</b> Removing one 'x' will make frequency of each distinct character to be 2.</pre>

<pre><b>Input: </b>s = "xxxxyyzz"
<b>Output: </b>false
<b>Explanation:</b> Frequency can not be made same by removing at most one character.</pre>

<b>Constraints:</b><br>1 ≤ s.size() ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Hash` `Strings` `Data Structures`
- **Company Tags:** `Zoho`

### Related Articles
- [Check If Frequency Of All Characters Can Become Same By One Removal](https://www.geeksforgeeks.org/check-if-frequency-of-all-characters-can-become-same-by-one-removal/)
