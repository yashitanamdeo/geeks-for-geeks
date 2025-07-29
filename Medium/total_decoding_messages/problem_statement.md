<h1 align="center">Total Decoding Messages</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 15.79%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 155K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

A message containing letters A-Z is being encoded to numbers using the following mapping:



'A' -> 1 <br>'B' -> 2 <br>... <br>'Z' -> 26 



You are given a string <b>digits</b>. You have to determine the <b>total number of ways</b> that message can be decoded.

<b>Examples:</b>

<pre><b>Input: </b>digits = "123"
<b>Output: </b>3
<b>Explanation: </b>"123" can be decoded as "ABC"(1, 2, 3), "LC"(12, 3) and "AW"(1, 23).
</pre>

<pre><b>Input: </b>digits = "90"<br><b>Output: </b>0
<b>Explanation: </b>"90" cannot be decoded, as it's an invalid string and we cannot decode '0'.<sup><br></sup></pre>

<pre><b>Input: </b>digits = "05"
<b>Output: </b>0
<b>Explanation: </b>"05" cannot be mapped to "E" because of the leading zero ("5" is different from "05"), the string is not a valid encoding message.</pre>

<b>Constraints:</b><br>1 ≤ digits.size() ≤ 10<sup>3</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Zoho` `Flipkart` `Morgan Stanley` `Amazon` `Microsoft` `OYO Rooms` `MakeMyTrip` `Goldman Sachs` `Nutanix` `Linkedin` `Facebook`

### Related Articles
- [Count Possible Decodings Given Digit Sequence](https://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/)

### Related Interview Experiences
- [Makemytrip Interview Experience Set 6 Online Coding](https://www.geeksforgeeks.org/makemytrip-interview-experience-set-6-online-coding/)
- [Flipkart Interview Experience Set 17 For Sde Ii](https://www.geeksforgeeks.org/flipkart-interview-experience-set-17-for-sde-ii/)
