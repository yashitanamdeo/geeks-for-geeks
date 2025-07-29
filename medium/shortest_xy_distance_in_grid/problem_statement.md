<h1 align="center">Shortest XY distance in Grid</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.35%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 24K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>N*M </b>grid of characters 'O', 'X', and 'Y'. Find the minimum Manhattan distance between a <b>X</b> and a <b>Y</b>.<br>
<br>
<u>Manhattan Distance</u> :<br>
<b>| row_index_x - row_index_y | + | column_index_x - column_index_y |</b>

<br>
<b>Example 1:</b>

<pre><b>Input:
</b>N = 4, M = 4
grid  = {{X, O, O, O}
         {O, Y, O, Y}
         {X, X, O, O}
         {O, Y, O, O}}
<b>Output:
</b>1
<b>Explanation:</b>
{{X, O, O, O}
{O, Y, O, Y}
{X, <b>X</b>, O, O}
{O, <b>Y</b>, O, O}}
The shortest X-Y distance in the grid is 1.
One possible such X and Y are marked in bold
in the above grid.</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N = 3, M = 3
grid = {{X, X, O}
        {O, O, Y}
        {Y, O, O}}
<b>Output :</b>
2
<b>Explanation:</b>
{{X, <b>X</b>, O}
 {O, O, <b>Y</b>}
 {Y, O, O}}
The shortest X-Y distance in the grid is 2.
One possible such X and Y are marked in bold
in the above grid.
</pre>

<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>shortestXYDist()</b> which takes two integers N, and M and an 2D list of size N*M as input and returns the shortest Manhattan Distance between a X and a Y.

<b>Expected Time Complexity:</b> O(N*M)<br>
<b>Expected Auxiliary Space:</b> O(N*M)

<br>
<b>Constraints:</b><br>
1 ≤ N*M ≤ 10<sup>5</sup><sup> </sup>

There exists at least one 'X' and at least one 'Y' in the grid.


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `BFS` `Algorithms`
- **Company Tags:** `Google`

### Related Articles
- [Shortest Xy Distance In Grid](https://www.geeksforgeeks.org/shortest-xy-distance-in-grid/)

### Related Interview Experiences
- [Google Interview Experience For Sde 1](https://www.geeksforgeeks.org/google-interview-experience-for-sde-1/?ref=rp)
