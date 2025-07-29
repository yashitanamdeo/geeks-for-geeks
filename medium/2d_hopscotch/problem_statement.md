<h1 align="center">2D Hopscotch</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 60.93%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 11K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 25m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Aakriti, Avantika and Mehak are playing 2D Hopscotch. The arena is in the form of a n*m 2D matrix. But the position of the cells is slightly modified as shown below. <br>
<img src="https://contribute.geeksforgeeks.org/wp-content/uploads/hopscotch-1.jpg" alt="" title=""/>

Mehak starts the game from tile (i,j) while Avantika and Aakriti direct her. In each turn Mehak will collect all the stones present (1 or 2) steps away from where she is standing. Avantika can direct Mehak to take 1 step and and Aakriti can direct Mehak to take 2 steps. <br>
If the director ty is known to you as ty = 0 being Avantika and 1 being Aakriti, find the number of stones that Mehak will collect. 

<br>
<b>Example 1:</b>

<pre><b>Input: </b>
n = 3, m = 3
mat = {{5, 9, 7}, 
       {6, 4, 5}, 
       {8, 1, 2}}
ty = 0, 
i = 1, j = 1
<b>Output:</b> 31
<b>Explaination: </b>
ty=0, so Avantika is the director. 
ie- Mehak will move only one step in 
any direction to collect the stones.
(0,1), (1,0), (1,2), (2,1), (2,2), (2,0) 
are at a distance of 1 from (1,1). 
Adding them 9+6+5+8+1+2=31.</pre>

<br>
<b>Example 2:</b>

<pre><b>Input: </b>
n = 3, m = 3
mat = {{5, 9, 7}, 
       {6, 4, 5}, 
       {8, 1, 2}}
ty = 1, 
i = 1, j = 1
<b>Output:</b> 12
<b>Explaination: </b>
ty=1, so Aakriti is the director. 
ie- Mehak can move 2 steps. 
(0,0) and (0,2) are the only tiles that 
are at a distance of two from (1,1). 
Adding them gives 5+7=12.</pre>

<br>
<b>Your Task:</b><br>
You do not need to read input or print anything. Your task is to complete the function <b>hopscotch() </b>which takes n, m, mat, ty, i and j as input parameters and returns the number of collected stones.

<br>
<b>Expected Time Complexity:</b> O(1)<br>
<b>Expected Auxiliary Space: </b>O(1)

<br>
<b>Constraints:</b><br>
1 ≤ n, m ≤ 1000000<br>
0 ≤ i < n<br>
0 ≤ j < m


<hr>

### Tags
- **Topic Tags:** `Matrix` `CPP` `Data Structures`
- **Company Tags:** `None`
