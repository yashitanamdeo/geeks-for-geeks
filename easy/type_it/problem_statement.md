<h1 align="center">Type it!</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.32%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 23K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Geek is extremely punctual but today even he is not feeling like doing his homework assignment. He must start doing it immediately in order to meet the deadline. For the assignment, Geek needs to type a string <b>s</b>.<br>
To reduce his workload, he has decided to perform one of the following two operations till he gets the string.

- Append a character at the end of the string.
- Append the string formed thus far to the end of the string. (This can not be done more than once.)
Help Geek find the minimum operations required to type the given string.

<br>
<b>Example 1:</b>

<pre><b>Input</b>:
s = abcabca
<b>Output:</b> 5
<b>Explanation</b>: a -> ab -> abc -> abcabc 
-> abcabca
</pre>

<br>
<b>Example 2:</b>

<pre><b>Input:</b>
s = abcdefgh
<b>Output: </b>8
<b>Explanation</b>: a -> ab -> abc -> abcd 
-> abcde -> abcdef -> abcdefg -> abcdefgh
</pre>

<br>
<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>minOperation()</b> which takes a string s<b> </b>as input parameter and returns the minimum operations required to type it.

<b>Expected Time Complexity:</b> O(N<sup>2</sup>)<br>
<b>Expected Auxiliary Space: </b>O(1)

<b>Constraints:</b><br>
1 <= N <= 10<sup>3</sup>


<hr>

### Tags
- **Topic Tags:** `Strings` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Find The Minimum Operations Required To Type The Given String](https://www.geeksforgeeks.org/find-the-minimum-operations-required-to-type-the-given-string/)
