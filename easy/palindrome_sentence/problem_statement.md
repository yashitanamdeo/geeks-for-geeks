<h1 align="center">Palindrome Sentence</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.04%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 41K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a single string <b>s</b>, the task is to check if it is a <b>palindrome sentence</b> or not.<br>A palindrome sentence is a sequence of characters, such as word, phrase, or series of symbols that reads the <b>same</b> backward as forward after converting all <b>uppercase </b>letters to<b> lowercase </b>and <b>removing</b> all <b>non-alphanumeric</b> characters (including spaces and punctuation).

<b>Examples:</b>

<pre><b>Input: </b>s = "Too hot to hoot"
<b>Output:</b> true
<b>Explanation:</b> If we remove all non-alphanumeric characters and convert all uppercase letters to lowercase, string s will become "toohottohoot" which is a palindrome.</pre>

<pre><b>Input: </b>s = "Abc 012..## 10cbA"
<b>Output:</b> true
<b>Explanation:</b> If we remove all non-alphanumeric characters and convert all uppercase letters to lowercase, string s will become "abc01210cba" which is a palindrome.</pre>

<pre><b>Input: </b>s = "ABC $. def01ASDF"<br><b>Output:</b> false<br><b>Explanation:</b> The processed string becomes "abcdef01asdf", which is not a palindrome.</pre>

<b>Constraints:</b><br>1 ≤ s.length() ≤ 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `two-pointer-algorithm` `Strings` `palindrome` `Data Structures` `Algorithms`
- **Company Tags:** `Facebook`

### Related Articles
- [Sentence Palindrome Palindrome Removing Spaces Dots Etc](https://www.geeksforgeeks.org/sentence-palindrome-palindrome-removing-spaces-dots-etc/)

### Related Interview Experiences
- [Facebook Interview Set 1](https://www.geeksforgeeks.org/facebook-interview-set-1/)
