<h1 align="center">Cutting Binary String</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.71%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 42K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a binary string <b>s</b> consisting only of characters <b>'0'</b> and <b>'1'</b>. Your task is to split this string into the <b>minimum number </b>of non-empty<b> substrings</b> such that:

- Each substring represents a <b>power of 5</b> in decimal (e.g., 1, 5, 25, 125, ...).<br>
- No substring should have <b>leading zeros</b>.
Return the <b>minimum number </b>of such pieces the string can be divided into.<br><b>Note:</b> If it is <b>not possible</b> to split the string in this way, return <b>-1</b>.

<b>Examples:</b>

<pre><b>Input: </b>s<b> = </b>"101101101"<b><br>Output: </b>3<b><br>Explanation: </b>The string can be split into three substrings: "101", "101", and "101", each of which is a power of 5 with no leading zeros.</pre>

<pre><b>Input:</b> s = "1111101"
<b>Output:</b> 1
<b>Explanation:</b> The string can be split into one binary string "1111101" which is 125 in decimal and a power of 5 with no leading zeros.</pre>

<pre><b>Input: </b>s = "00000"<br><b>Output: </b>-1<br><b>Explanation: </b>There is no substring that can be split into power of <b>5.<br></b></pre>

<b>Constraints:<br></b>1 ≤ s.size() ≤ 30

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Strings` `Dynamic Programming` `Bit Magic` `Data Structures` `Algorithms`
- **Company Tags:** `Flipkart` `Walmart` `Google`

### Related Articles
- [Minimum Number Of Sub Strings Of A String Such That All Are Power Of 5](https://www.geeksforgeeks.org/minimum-number-of-sub-strings-of-a-string-such-that-all-are-power-of-5/)

### Related Interview Experiences
- [Flipkart Interview Set 11](httpss://www.geeksforgeeks.org/flipkart-interview-set-11/)
