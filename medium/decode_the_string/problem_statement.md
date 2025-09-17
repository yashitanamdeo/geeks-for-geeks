<h1 align="center">Decode the string</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 44.28%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 67K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 10m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an encoded string s, decode it by expanding the pattern k[substring], where the substring inside brackets is written <b>k</b> times. k is guaranteed to be a positive integer, and encodedString contains only lowercase english alphabets. Return the <b>final decoded string</b>.

<b>Note: </b>The test cases are generated so that the length of the output string will never exceed 10<sup>5</sup> .

<b>Examples:</b>

<pre><b>Input:</b> s = "3[b2[ca]]"
<b>Output:</b> "bcacabcacabcaca"
<b>Explanation:<br></b>Inner substring “2[ca]” breakdown into “caca”.<br>Now, new string becomes “3[bcaca]”
Similarly “3[bcaca]” becomes “bcacabcacabcaca” which is final result.<br></pre>

<pre><b>Input:</b> s = "3[ab]"
<b>Output:</b> "ababab"
<b>Explanation:</b> The substring "ab" is repeated 3 times giving "ababab".</pre>

<b>Constraints:</b><br>1 ≤ |s| ≤ 10<sup>5</sup> <br>1 ≤ k ≤ 100

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Recursion` `Stack` `Backtracking` `Data Structures` `Algorithms`
- **Company Tags:** `Microsoft` `Facebook`

### Related Articles
- [Decode String Recursively Encoded Count Followed Substring](https://www.geeksforgeeks.org/decode-string-recursively-encoded-count-followed-substring/)
