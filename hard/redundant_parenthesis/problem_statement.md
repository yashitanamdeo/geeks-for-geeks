<h1 align="center">Redundant Parenthesis</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.49%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 26K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a valid expression containing only binary operators <b>'+', '-', '*', '/' </b>and operands, remove all the redundant parenthesis.


A set of parenthesis is said to be redundant if, removing them, does not change the value of the expression.


<b>Note: </b>The operators <b>'+'</b> and <b>'-'</b> have the same priority. <b>'*'</b> and <b>'/'</b> also have the same priority. <b>'*'</b> and <b>'/'</b> have more priority than <b>'+'</b> and <b>'-'</b>.

<br><b>Example 1:</b>

<pre><b>Input</b>:
Exp = (A*(B+C))
<b>Output:</b> A*(B+C)
<b>Explanation</b>: The outermost parenthesis
are redundant.
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
Exp = A+(B+(C))
<b>Output: </b>A+B+C
<b>Explanation</b>: All the parenthesis
are redundant.</pre>

<br><b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>removeBrackets()</b> which takes the string <b>Exp </b>as input parameters and returns the updated expression.

<br><b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(N)

<br><b>Constraints:</b><br>1 <u><</u> Length of Exp <u><</u> 10<sup>5</sup><br>Exp contains uppercase english letters, '(' , ')', '+', '-', '*' and '/'.


<hr>

### Tags
- **Topic Tags:** `Strings` `Stack` `Data Structures`
- **Company Tags:** `Oracle`

### Related Articles
- [Remove All Redundant Parenthesis](https://www.geeksforgeeks.org/remove-all-redundant-parenthesis/)

### Related Interview Experiences
- [Oracle Interview Experience For Application Developer On Campus Virtual](https://www.geeksforgeeks.org/oracle-interview-experience-for-application-developer-on-campus-virtual/)
