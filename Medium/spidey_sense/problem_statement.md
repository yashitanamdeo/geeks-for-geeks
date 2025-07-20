<h1 align="center">Spidey Sense</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 70.34%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 6K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Spiderman is stuck in a difficult situation. His arch-enemy the Green Goblin has planted several of his infamous Pumpkin Bombs in various locations in a building. Help Spiderman activate his Spidey Sense and identify the impact zones. <br>
He has a blueprint of the building which is a M x N matrix that is filled with the characters O, B, and W where: <br>
O represents an open space.<br>
B represents a bomb.<br>
W represents a wall.<br>
You have to replace all of the Os (open spaces) in the matrix with their shortest distance from a bomb without being able to go through any walls. Also, replace the bombs with 0 and walls with -1 in the resultant matrix. If no path exists between a bomb and an open space replace the corresponding 'O' with -1.

<b>Example 1:</b>

<pre><b>Input: </b>N = 3, M = 3
A[] = {{O, O, O}, 
       {W, B, B}, 
       {W, O, O}}
<b>Output:</b> {{2, 1, 1}, 
         {-1, 0, 0},  
         {-1, 1, 1}}
<b>Explanation: </b>The walls at (1,0) and (2,0) 
are replaced by -1. The bombs at (1,1) and 
(1,2) are replaced by 0.<b> The impact zone 
for the bomb at (1,1)</b> includes open spaces 
at index (0,0), (0,1) and (2,1) with distance 
from bomb calculated as 2,1,1 respectively.
<b>The impact zone for the bomb at (1,2)</b> 
includes open spaces at index (0,3) and (2,2) 
with distance from bomb calculated as 1,1 
respectively.
</pre>

<br>
<b>Example 2:</b>

<pre><b>IInput: </b>N = 2, M = 2
A[] = {{O, O},
       {O, O}} 
<b>Output:</b> {{-1, -1}
         {-1, -1}
</pre>

<b>Your Task: </b> <br>
You don't need to read input or print anything. Complete the function <b>findDistance()</b> which takes the matrix A[], M, and N as input parameters and the resultant matrix

<b>Expected Time Complexity:</b> O(M*N)<br>
<b>Expected Auxiliary Space:</b> O(M*N)

<br>
<b>Constraints:</b><br>
1 ≤ N*M ≤ 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Graph` `Queue` `BFS` `Data Structures` `Algorithms`
- **Company Tags:** `None`
