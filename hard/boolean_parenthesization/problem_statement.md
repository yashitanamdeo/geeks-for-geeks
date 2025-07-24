<h1 align="center">Boolean Parenthesization</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 20.15%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 141K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a boolean expression <b>s </b>containing<br>    'T' ---> true<br>    'F' ---> false <br>and following operators between symbols<br>   &   ---> boolean AND<br>    |   ---> boolean OR<br>   ^   ---> boolean XOR<br>Count the number of ways we can <b>parenthesize </b>the expression so that the value of expression evaluates to <b>true</b>.

Note: The answer is guaranteed to fit within a <b>32-bit</b> integer.

<b>Examples:</b>

<pre><b>Input:</b> s = "T|T&F^T"
<b>Output:</b> 4
<b>Explaination:</b> The expression evaluates to true in 4 ways: ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T)).</pre>

<pre><b>Input:</b> s = "T^F|F"
<b>Output:</b> 2
<b>Explaination:</b> The expression evaluates to true in 2 ways: ((T^F)|F) and (T^(F|F)).</pre>

<b>Constraints:</b><br>1 ≤ |s| ≤ 100

## Expected Complexities
- Time Complexity: O(n^3)
- Auxiliary Space: O(n^2)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Amazon` `Microsoft` `Intuit` `Linkedin`

### Related Articles
- [Boolean Parenthesization Problem Dp 37](https://www.geeksforgeeks.org/boolean-parenthesization-problem-dp-37/)

### Related Interview Experiences
- [Intuit Interview Experience On Campus 2021](https://www.geeksforgeeks.org/intuit-interview-experience-on-campus-2021/)
