<h1 align="center">Count Cyclic Paths</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 52.24%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 22K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>triangular pyramid</b> with its vertices marked as <b>O, A, B and C</b> and a number <b>N</b>, the task is to find the number of ways such that a person starting from the origin <b>O</b> initially, reaches back to the origin in <b>N</b> steps. In a single step, a person can go to any of its adjacent vertices.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20200520133822/pyramid1.jpg" alt="Lightbox" title=""/>

<br>
<b>Example 1:</b>

<pre><b>Input</b>:
N = 1
<b>Output:</b> 0
<b>Explanation</b>: The minimum length of
a cyclic path is 2.
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N = 2
<b>Output: </b>3
<b>Explanation</b>: The three paths are :
O-A-O, O-B-O, O-C-O</pre>

<br>
<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>countPaths()</b> which takes an integer N<b> </b>as input parameter and returns the number of possible paths. Since the answer may be big, return it modulo <b>(10^9+7)</b>. 

<br>
<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Auxiliary Space:</b> O(1)

<br>
<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `OYO Rooms`

### Related Articles
- [Count Of Ways To Travel A Cyclic Path In N Steps In A Triangular Pyramid](https://www.geeksforgeeks.org/count-of-ways-to-travel-a-cyclic-path-in-n-steps-in-a-triangular-pyramid/)

### Related Interview Experiences
- [Oyo Interview Experience For Sde 1 On Campus 2](https://www.geeksforgeeks.org/oyo-interview-experience-for-sde-1-on-campus-2/)
