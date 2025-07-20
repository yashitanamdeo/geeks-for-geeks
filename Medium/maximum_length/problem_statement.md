<h1 align="center">Maximum Length</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 55.93%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 28K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given the maximum occurrences of a, b, and c in a string. Your task is to make the string containing only a, b, and c such that no three consecutive characters are the same. If the resultant string equals to a+b+c, return the length (a+b+c) otherwise -1.

<b>Example 1:</b>

<pre><b>Input</b>:
a = 3, b = 3, c = 3<b>
Output:</b> 
9<b>
Explanation</b>: 
No three consecutive character of
the string "abcabcabc" is same.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
a = 11, b = 2, c = 2<b>
Output: </b>
-1<b>
Explanation</b>: 
If we build a string of these character's,
the string will be"aabaacaabaac<u><b>aaa</b></u>", here
we can see that there will be three consecutive <b>a</b>. So
there is no solution exist.</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>solve( )</b> which takes <b>integers a, b, and c</b> as input parameters and <b>returns </b>the <b>string length</b>. If there is no possible answer return -1.

<b>Expected Time Complexity:</b> O(a+b+c)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>0 ≤ a, b, c ≤ 10<sup>5</sup><br>0 < (a + b + c)


<hr>

### Tags
- **Topic Tags:** `Strings` `Data Structures`
- **Company Tags:** `None`
