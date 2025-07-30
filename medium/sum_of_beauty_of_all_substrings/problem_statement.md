<h1 align="center">Sum of Beauty of All Substrings</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 57.41%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 21K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string<b> S</b>, return the sum of <b>beauty</b> of all its substrings.<br>The <b>beauty</b> of a string is defined as the difference in frequencies between the most frequent and least frequent characters.

- For example, the beauty of string "aaac" is 3 - 1 = 2.
<b>Example 1:</b>

<b>Input:</b><br>S = "aaac"<br><b>Output: </b><br>3<br><b>Explanation: </b>The substrings with non - zero beauty are ["aaac","aac"] <br>where beauty of "aaac" is 2 and beauty of "aac" is 1.
 

<b>Example 2:</b>

<b>Input:</b><br>S = "geeksforgeeks"<br><b>Output: </b><br>62<br><b>Explanation:</b> There are 91 substrings of the given strings.<br>Like, the beauty of substring "geek" is 1. <br>In this way the sum of beauties of all substrings are 62.
<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>beautySum()</b> which takes string <b>S</b> as input paramters and returns the sum of <b>beauty</b> of all its substrings. 

<b>Expected Time Complexity: </b>O(|S|<sup>2</sup>)<br><b>Expected Auxiliary Space: </b>O(1)

<b>Constraints: </b><br>1 ≤ |S| ≤ 500<br>S only contains lower case alphabets.


<hr>

### Tags
- **Topic Tags:** `Strings` `Data Structures`
- **Company Tags:** `None`
