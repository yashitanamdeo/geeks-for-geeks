<h1 align="center">Stream First Non-repeating</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 31.65%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 220K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an input stream <b>s</b> consisting only of lowercase alphabets. While reading characters from the stream, you have to tell which character has appeared only once in the stream upto that point. If there are many characters that have appeared only once, you have to tell which one of them was the first one to appear. If there is no such character then append '#' to the answer.

<b>NOTE:<br></b>1. You need to find the answer for every i (0 <= i < n)<br>2. In order to find the solution for every you need to consider the string from starting position till the ith position.<b><br></b> 

<b>Examples:</b>

<pre><b>Input: </b>s = "aabc"
<b>Output: </b>"a#bb"
<b>Explanation: </b>For every ith character we will consider the string from index 0 till index i first non repeating character is as follow- "a" - first non-repeating character is 'a' "aa" - no non-repeating character so '#' "aab" - first non-repeating character is 'b' "aabc" - there are two non repeating characters 'b' and 'c',  first non-repeating character is 'b' because 'b' comes before 'c' in the stream.</pre>

<pre><b>Input: </b>s = "zz"
<b>Output: </b>"z#"
<b>Explanation: </b>For every character first non repeating character is as follow- "z" - first non-repeating character is 'z' "zz" - no non-repeating character so '#' </pre>

<pre><b>Input: </b>s = "bb"
<b>Output: </b>"b#"
<b>Explanation: </b>For every character first non repeating character is as follow- "b" - first non-repeating character is 'b' "bb" - no non-repeating character so '#'  </pre>

<b>Constraints:</b><br>1 <= s.size()<= 10<sup>5<br>'a' <= s[i] <= 'z'</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Hash` `Queue` `Data Structures`
- **Company Tags:** `Flipkart` `Amazon` `Microsoft` `FactSet` `Payu` `Adobe` `Yahoo`

### Related Articles
- [Find First Non Repeating Character Stream Characters](https://www.geeksforgeeks.org/find-first-non-repeating-character-stream-characters/)

### Related Interview Experiences
- [Flipkart Interview For Sde Ii 2](https://www.geeksforgeeks.org/flipkart-interview-for-sde-ii-2/)
