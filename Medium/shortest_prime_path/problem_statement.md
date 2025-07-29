<h1 align="center">Shortest Prime Path</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 63.49%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 28K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given two four digit prime numbers <b>num1 </b>and <b>num2.</b> Find the distance of the shortest path from Num1 to Num2 that can be attained by altering only single digit at a time such that every number that we get after changing a digit is a four digit prime number with no leading zeros.

<b>Example 1:</b>

<pre><b>Input:</b>
num1 = 1033 
num2 = 8179
<b>Output: </b>6
<b>Explanation:</b>
1033 -> 1<b>7</b>33 -> <b>3</b>733 -> 373<b>9</b> -> 37<b>7</b>9 -> <b>8</b>779 -> 8<b>1</b>79.
There are only 6 steps reuired to reach num2 from num1. 
and all the intermediate numbers are 4 digit prime numbers.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
num1 = 1033 
num2 = 1033
<b>Output:</b>
0</pre>

<b>Your Task:</b>  <br>You don't need to read input or print anything. Your task is to complete the function <b>solve</b>() which takes two integers num1 and num2 as input parameters and returns the distance of the shortest path from num1 to num2. If it is unreachable then return -1.

<b>Expected Time Complexity:</b> O(nlogn)<br><b>Expected Auxiliary Space:</b> O(n)

<b>Constraints:</b><br>1000<=num1,num2<=9999<br>num1 and num2 are prime numbers.


<hr>

### Tags
- **Topic Tags:** `Prime Number` `Shortest Path` `BFS` `Algorithms`
- **Company Tags:** `Adobe`

### Related Articles
- [Shortest Path Reach One Prime Changing Single Digit Time](https://www.geeksforgeeks.org/shortest-path-reach-one-prime-changing-single-digit-time/)

### Related Interview Experiences
- [Adobe Interview Experience 4](https://www.geeksforgeeks.org/adobe-interview-experience-4/)
