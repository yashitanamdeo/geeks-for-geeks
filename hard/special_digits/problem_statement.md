<h1 align="center">Special Digits</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.3%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 28K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given 5 integers - <b>N,A,B,C,D</b>.<br>
Let us say all the integers of length <b>N</b>, having only <b>A </b>or <b>B</b> in their decimal representation are <b>good </b>integers. Also, among all the good integers, all those integers whose sum of digits should <b>contains </b>either C or D or both on it, are <b>best </b>integers.<br>
Find the number of best integers of length <b>N</b>. Since the number of best integers can be huge, print it modulo <b>10<sup>9</sup>+7</b>.<br>
<b>Example 1:</b>

<pre><b>Input:
</b>N = 2, A = 1, B = 2, C = 3, D = 5
<b>Output: 
</b>2<b>
Explanation: 
</b>The following are good integers:- 
{ 12 , 22 , 11 , 21 }
And the following are best integers:- 
{ 12, 21 } because sum of digits 3 & 5
contains C & D, which is 3 as well as 5.
</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N = 1, A = 1, B = 1, C = 2, D = 3
<b>Output: 
</b>0<b>
Explanation: 
</b>The following are good integers: - { 1 }
Since sum of digits is 1 which does not contains
C or D, therefore, answer is 0.</pre>

<b>Example 3:</b>

<pre><b>Input:
</b>N = 4, A = 6, B = 7, C = 5, D = 3
<b>Output: 
</b><b>4
Explanation: 
</b>The following are good integers:- 
{ 6667 , 6676 , 6766 , 7666.....and many more}
out of all these four { 6667 , 6676 , 6766 , 7666}
is best number because sum of all these four 
numbers is 25, which contains C, which is 5.</pre>

<b>Your Task:</b><br>
The task is to complete the function <b>solve()</b> which takes five integers <b>N,A,B,C</b> and <b>D</b> as input parameters and returns the number of best integers modulo 10<sup>9</sup>+7.

<b>Expected Time Complexity: O(NlogN)<br>
Expected Space Complexity: O(N)</b>

<b>Constraints:</b><br>
1 ≤ A, B, C, D ≤ 9<br>
1 ≤ N ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Combinatorial` `Mathematical`
- **Company Tags:** `None`
