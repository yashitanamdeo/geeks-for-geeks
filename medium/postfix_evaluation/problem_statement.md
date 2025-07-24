<h1 align="center">Postfix Evaluation</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 63.04%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 114K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array of strings <b>arr</b> that represents a valid arithmetic expression written in <b>Reverse Polish Notation (Postfix Notation)</b>. Your task is to evaluate the expression and return an integer representing its value.

<b>Key Details</b>:

1. The valid operators are <b>'+'</b>, <b>'-'</b>, <b>'*'</b>, and <b>'/'</b>.
1. Each operand is guaranteed to be a valid integer or another expression.
1. The division operation between two integers always rounds the result towards zero, discarding any fractional part.
1. No division by zero will occur in the input.
1. The input is a valid arithmetic expression in Reverse Polish Notation.
1. The result of the expression and all intermediate calculations will fit in a 32-bit signed integer.
<b>Examples:</b>

<pre><b>Input: </b>arr = ["2", "3", "1", "*", "+", "9", "-"]<br><b>Output:</b> -4<br><b>Explanation:</b> If the expression is converted into an infix expression, it will be 2 + (3 * 1) – 9 = 5 – 9 = -4.</pre>

<pre><b>Input:</b> arr = ["100", "200", "+", "2", "/", "5", "*", "7", "+"]<br><b>Output:</b> 757<br><b>Explanation:</b> If the expression is converted into an infix expression, it will be ((100 + 200) / 2) * 5 + 7  = 150 * 5 + 7 = 757.</pre>

<b>Constraints:</b>

- 1 <= arr.size() <= 10<sup>5</sup>
- arr[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-10<sup>4</sup>, 10<sup>4</sup>]

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Stack` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Stack Set 4 Evaluation Postfix Expression](https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/)
