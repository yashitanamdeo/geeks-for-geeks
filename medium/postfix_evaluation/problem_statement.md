<h1 align="center">Postfix Evaluation</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 63.04%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 125K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array of strings <b>arr[]</b> that represents a valid arithmetic expression written in <b>Reverse Polish Notation </b>(Postfix Notation). Your task is to evaluate the expression and return an integer representing its value.

<b>Note: </b>A postfix expression is of the form operand1 operand2 operator (e.g., "a b +"). <br>And the division operation between two integers always computes the <b>floor value,</b> i.e floor(5 / 3) = 1 and floor(-5 / 3) = -2.<br>It is guaranteed that the result of the expression and all intermediate calculations will fit in a 32-bit signed integer.

<b>Examples:</b>

<pre><b>Input:</b> arr[] = ["2", "3", "1", "*", "+", "9", "-"]
<b>Output:</b> -4
<b>Explanation:</b> If the expression is converted into an infix expression, it will be 2 + (3 * 1) – 9 = 5 – 9 = -4.</pre>

<pre><b>Input:</b> arr[] = ["2", "3", "^", "1", "+"]
<b>Output:</b> 9
<b>Explanation:</b> If the expression is converted into an infix expression, it will be 2 ^ 3 + 1 = 8 + 1 = 9.</pre>

<b>Constraints:<br></b>3 ≤ arr.size() ≤ 10<sup>3</sup><sup><br></sup>arr[i] is either an operator: "+", "-", "*", "/" or "^", or an integer in the range [-10<sup>4</sup>, 10<sup>4</sup>]

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Stack` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Stack Set 4 Evaluation Postfix Expression](https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/)
