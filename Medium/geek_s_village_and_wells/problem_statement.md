<h1 align="center">Geek's Village and Wells</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 57.11%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 23K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Geek's village is represented by a 2-D matrix of characters of size n*m, where

H - Represents a house<br>
W - Represents a well<br>
. - Represents an open ground<br>
N - Prohibited area(Not allowed to enter this area)

Every house in the village needs to take water from a well, as the family members are so busy with their work, so every family wants to take the water from a well in minimum time, which is possible only if they have to cover as less distance as possible. Your task is to determine the minimum distance that a person in the house should travel to take out the water and carry it back to the house.

A person is allowed to move only in four directions left, right, up, and down. That means if he/she is the cell (i,j), then the possible cells he/she can reach in one move are (i,j-1),(i,j+1),(i-1,j),(i+1,j), and the person is not allowed to move out of the grid.

<b>Note:</b> For all the cells containing 'N', 'W' and '.' our answer should be 0, and for all the houses where there is no possibility of taking water our answer should be -1.

<b>Example 1:</b>

<pre><b>Input:</b>
n = 3
m = 3
c[][]: H H H
       H W H
       H H H
<b>Output:</b>
4 2 4 
2 0 2 
4 2 4
<b>Explanation:</b>
There is only one well hence all the houses present
in the corner of matrix will have to travel a minimum
distance of 4, 2 is for house to well and other two is
for well to house. And rest of the houses have to travel
a minimum distance of 2 (House -> Well -> House).</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
n = 5
m = 5
c[][]: H N H H H
       N N H H W
       W H H H H
       H H H H H
       H H H H H
<b>Output:</b>
-1 0 6 4 2 
0 0 4 2 0 
0 2 4 4 2 
2 4 6 6 4 
4 6 8 8 6
<b>Explanation:</b>
There is no way any person from the house in
cell (0,0) can take the water from any well, and
for rest of the houses there is same type of
strategy we have to follow as followed in example 1. </pre>

<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function geekAndWells() which takes n and m, dimensions of the grid, and a 2-D grid of size n*m and returns a 2-D array containing the minimum distance for all the houses as explained above.

<b>Expected Time Complexity: O(n*m)<br>
Expected Space Complexity: O(n*m)</b>

<b>Constraints:</b><br>
1 <= n <= 10^3<br>
1 <= m <= 10^3


<hr>

### Tags
- **Topic Tags:** `Matrix` `BFS` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Minimum Distance To Fetch Water From Well In A Village](https://www.geeksforgeeks.org/minimum-distance-to-fetch-water-from-well-in-a-village/)
