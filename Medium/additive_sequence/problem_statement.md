<h1 align="center">Additive sequence</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 52.99%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 36K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>n</b>, your task is to find whether it contains an <b>additive sequence or not</b>. A string <b>n </b>contains an additive sequence if its digits can make a <b>sequence of numbers</b> in which every number is <b>addition of previous two numbers (within the range of signed integers)</b>. You are required to complete the function which returns <b>true</b> if the string is a valid sequence else returns <b>false</b>. For better understanding check the examples.

<b>Note: </b>A valid string should contain at <b>least three</b> digit to make one additive sequence. 

<b>Example 1:</b>

<pre><b>Input:</b>  <br>n = "1235813"
<b>Output:</b> <br>1
<b>Explanation:</b> <br>The given string can be splited into a series of numbers  <br>where each number is the sum of the previous two numbers: <br>1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8, and 5 + 8 = 13. Hence, the output would be 1 (true).<br></pre>

<b>Example 2:</b>

<pre><b>Input:</b>  <br>n = "11235815"
<b>Output:</b> <br>0
<b>Explanation:</b> <br>We can start with the first two digits: "11".
First number: 1, Second number: 1, Sum: 1 + 1 = 2
Now, we have "2" as the next number.
First number: 1, Second number: 2, Sum: 1 + 2 = 3
Now, we have "3" as the next number.
First number: 2, Second number: 3, Sum: 2 + 3 = 5
Now, we have "5" as the next number.
First number: 3, Second number: 5, Sum: 3 + 5 = 8
Now, we have "8" as the next number.
First number: 5, Second number: 8, Sum: 5 + 8 = 13
At this point, there is no "13" present in the remaining digits "815". Hence, the output would be 0 (or false).<br></pre>

<b>User Task: </b><br>Your task is to complete the function <b>isAdditiveSequence()</b> which takes a single string as input <b>n</b> and returns a <b>boolean value</b> indicating whether the given string contains an <b>additive sequence or not</b>. You need not take any input or print anything.

<b>Expected Time Complexity: </b>O(n<sup>3</sup>).<br><b>Expected Auxiliary Space: </b>O(n).

<b>Constraints:</b><br>3 <= length( n ) <= 200<br>1 <= digits of string <= 9


<hr>

### Tags
- **Topic Tags:** `Strings` `Recursion` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [String With Additive Sequence](https://www.geeksforgeeks.org/string-with-additive-sequence/)
