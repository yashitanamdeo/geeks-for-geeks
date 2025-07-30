<h1 align="center">Bleak Numbers</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.12%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 61K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an integer, check whether it is <b>Bleak or not</b>. 

A number n is called Bleak if it <b>cannot </b>be represented as sum of a positive number x and set bit count in x, i.e., x + [countSetBits(x)](http://www.geeksforgeeks.org/count-set-bits-in-an-integer/) is not equal to n for any non-negative number x.

<b>Example 1:</b>

<pre><b>Input: <br></b>4
<b>Output: <br></b>0
<b>Explanation: <br></b>There is no x such that x + countSetbit(x) = 4
</pre>

<b>Example 2:</b>

<pre><b>Input:</b> <br>3
<b>Output: <br></b>1
<b>Explanation:</b> <br>3 is a Bleak number as 2 + countSetBit(2) = 3.
</pre>

<b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>is_bleak()</b> which takes n as input parameter and <b>returns 0</b> if n is <b>not </b>a Bleak number otherwise <b>returns 1</b>.<br><b><br>Expected Time Complexity: </b>O(log(n) * log(n))<br><b>Expected Space Complexity: </b>O(1)<br> <br><b>Constraints:</b><br>1 <= n <= 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Bit Magic` `Data Structures`
- **Company Tags:** `SAP Labs`

### Related Articles
- [Check If A Number Is Bleak](https://www.geeksforgeeks.org/check-if-a-number-is-bleak/)
