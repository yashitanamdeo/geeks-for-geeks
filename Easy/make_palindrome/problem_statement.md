<h1 align="center">Make Palindrome</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 55.43%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 34K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array of strings <b>arr</b> of size<b> n</b>. You have to find out if it is possible to make a palindromic string by concatenating all the strings in any order. Provided that all the strings given in the array are of <b>equal length</b>.

<b>Example 1:</b>

<pre><b>Input:</b>
n = 4
arr = {"djfh", "gadt", "hfjd", "tdag"}
<b>Output:</b>
YES
<b>Explanation:</b>
You can make the string "djfhgadttdaghfjd", by concatenating the given strings which is a palindrome.
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
n = 3
arr = {"jhjdf", "sftas", "fgsdf"}
<b>Output:</b>
NO
<b>Explanation:</b>
You can't make a palindromic string with this strings.
</pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>makePalindrome()</b> which takes an integer <b>n</b> and an array of strings <b>arr</b> respectively and returns <b>true</b> or <b>false</b>.

<b>Expected Time Complexity:</b> O(n * len(arr[i]))<br>
<b>Expected Space Complexity:</b> O(n * len(arr[i]))

<b>Constraints:</b><br>
1 <= n <= 10<sup>4</sup><br>
0 <= |arr[i]| <= 10<sup>4</sup><br>
The sum of n*|arr[i]| over all test cases won't exceed 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Strings` `palindrome` `Data Structures` `Algorithms`
- **Company Tags:** `None`
