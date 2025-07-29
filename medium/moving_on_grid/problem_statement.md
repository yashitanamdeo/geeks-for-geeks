<h1 align="center">Moving on grid</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 61.84%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 4K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a grid on XY plane with dimensions r x c, the two players (say JON and ARYA ) can move the coin over the grid satisfying the following rules:

- There is a coin on (1,1) cell initially.
- JON will move first.
- Both will play on alternate moves.
- In each move they can place coin on following positions if current position of coin is x,y<br>(x+1,y), (x+2,y), (x+3,y), (x,y+1), (x,y+2), (x,y+3), (x,y+4), (x,y+5), (x,y+6)
- They can't go outside the grid.
- Player who cannot make any move will lose this game.
- Both play optimally.
<br><b>Example 1:</b>

<pre><b>Input</b>: r = 1, c = 2
<b>Output:</b> JON 
<b>Explanation</b>: ARYA lost the game because
he won't able to move after JON's move.  
</pre>

<br><b>Example 2:</b>

<pre><b>Input: </b>r = 2, c = 2
<b>Output: </b>ARYA
<b>Explanation</b>: After first move by JON(1,2 or 2,1)
and second move by ARYA(2,2) JON won't able to
move so ARYA wins.   
</pre>

<br><b>Your Task:  </b><br>You dont need to read input or print anything. Complete the function <b>movOnGrid() </b>which takes r and c as input parameter and returns the name of the winner ( either JON or ARYA).<br><br><b>Expected Time Complexity:</b> O(1)<br><b>Expected Auxiliary Space:</b> O(1)<br><br><b>Constraints:</b><br>1 <= r, c <=10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Game Theory`
- **Company Tags:** `None`
