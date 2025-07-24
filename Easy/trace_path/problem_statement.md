<h1 align="center">Trace Path</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.66%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 30K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 10m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There is a rectangular path for a Train to travel consisting of <b>n </b>rows and <b>m</b> columns. The train will start from one of the grid's cells and it will be given a command in the form of string <b>s</b> consisting of characters <b>L</b>, <b>R</b>,<b> D</b>, <b>U</b>. Find if it is possible to travel the train inside the grid only.<br><b>Note: <br></b>If the train is at position (i,j) <br>on taking 'L' it goes to (i,j-1),<br>on taking 'R' it goes to (i,j+1),<br>on taking 'D' it goes to (i-1,j),<br>on taking 'U' it goes to (i+1,j).<br>You just need to tell if it's possible or not, you don't have to tell number of ways in which it is possible.

<b>Example 1:</b>

<pre><b>Input:</b> 
n = 1, m = 1
s = "R"
<b>Output:</b> 0
<b>Explaination:</b> There is only one cell(1,1). So train can only start from (1,1). On taking right(R) train moves to (1,2), which is out of grid.<br>Therefore there is no cell from where train can start and remain inside the grid after tracing the route. </pre>

<b>Example 2:</b>

<pre><b>Input:</b> 
n = 2, m = 3
s = "LLRU"
<b>Output:</b> 1
<b>Explaination:</b> One possible cell is (1,3)<br>(1,3) --> (1,2) --> (1,1) --> (1,2) --> (2,2). Thus there is a cell from where if train starts, it remains inside the grid throughout tracing the route.</pre>

<b>Your Task:</b><br>You do not need to read input or print anything. Your task is to complete the function <b>isPossible()</b> which takes n, m and s as input parameters and <b>returns 1</b> if there is such a cell for which the train always remains inside the grid. Otherwise <b>returns</b> <b>0</b>.

<b>Expected Time Complexity:</b> O(|s|)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>1 ≤ n, m ≤ 10<sup>4</sup><br>1 ≤ |s| ≤ 10<sup>4</sup>


<hr>

### Tags
- **Topic Tags:** `Matrix` `Data Structures`
- **Company Tags:** `None`
