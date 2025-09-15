<h1 align="center">String stack</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 46.69%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 19K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given two strings <b>pat </b>and <b>tar</b> consisting of lowercase English characters. You can construct a new string <b>s</b> by performing any one of the following operation for each character in pat:

- <b>Append</b> the character <b>pat[i] </b>to the string <b>s</b>.
- <b>Delete</b> the <b>last</b> character of <b>s </b>(if s is empty do nothing).
After performing operations on every character of <b>pat exactly once</b>, your goal is to determine if it is possible to make the string <b>s </b>equal to string <b>tar.</b>

<b>Examples:</b>

<pre><b>Input: </b>pat = "geuaek", tar = "geek"<br><b>Output: </b>true<br><b>Explanation: </b>Append the first three characters of pat to s, resulting in s = "geu". Delete the last character for 'a', leaving s = "ge". Then, append the last two characters 'e' and 'k' from pat to s, resulting in s = "geek", which matches tar.</pre>

<pre><b>Input: </b>pat = "agiffghd", tar = "gfg"<br><b>Output: </b>true<br><b>Explanation: </b>Skip the first character 'a' in pat. Append 'g' and 'i' to s, resulting in s = "gi". Delete the last character for 'f', leaving s = "g". Append 'f', 'g', and 'h' to s, resulting in s = "gfgh". Finally, delete the last character for 'd', leaving s = "gfg", which matches tar.</pre>

<pre><b>Input: </b>pat = "ufahs", tar = "aus"<br><b>Output: </b>false<br><b>Explanation: </b>It is impossible to construct the string tar from pat with the given operations.<br></pre>

<b>Constraints:<br></b>1 ≤ pat.size(), tar.size() ≤ 10<sup>5</sup><br>

## Expected Complexities
- Time Complexity: O(n + m)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Strings` `Greedy` `two-pointer-algorithm`
- **Company Tags:** `None`
