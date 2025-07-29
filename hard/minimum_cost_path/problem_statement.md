<h1 align="center">Minimum Cost Path</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 26.99%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 123K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a square <b>grid </b>of size <b>N</b>, each cell of which contains an integer cost that represents a cost to traverse through that cell, we need to find a <b>path</b> from the <b>top</b> <b>left</b> cell to the <b>bottom</b> <b>right</b> cell by which the total cost incurred is <b>minimum</b>.<br>From the cell (i,j) we can go (i,j-1), (i, j+1), (i-1, j), (i+1, j).  

<b>Examples :</b>

<pre><b>Input: </b>grid = [[9,4,9,9],<br>               [6,7,6,4],<br>               [8,3,3,7],<br>               [7,4,9,10]]
<b>Output: </b>43
<b>Explanation: </b>The minimum cost is-
9 + 4 + 7 + 3 + 3 + 7 + 10 = 43.
</pre>

<pre><b>Input: </b>grid = [[4,4],<br>               [3,7]]
<b>Output: </b>14
<b>Explanation: </b>The minimum cost is- 4 + 3 + 7 = 14.
</pre>

<pre><b>Constraints:</b><br>1 ≤ n ≤ 500<br>1 ≤ cost of cells ≤ 500</pre>

## Expected Complexities
- Time Complexity: O(n^2*log(n))
- Auxiliary Space: O(n^2)

<hr>

### Tags
- **Topic Tags:** `Graph` `Data Structures` `Algorithms` `Dynamic Programming` `Heap`
- **Company Tags:** `Amazon` `Microsoft` `Samsung` `MakeMyTrip` `Goldman Sachs`

### Related Articles
- [Minimum Cost Path Left Right Bottom Moves Allowed](https://www.geeksforgeeks.org/minimum-cost-path-left-right-bottom-moves-allowed/)

### Related Interview Experiences
- [Makemytrip Interview Experience Set 2 Campus](https://www.geeksforgeeks.org/makemytrip-interview-experience-set-2-campus/)
- [Samsung Interview Experience Through Co Cubes 2019](https://www.geeksforgeeks.org/samsung-interview-experience-through-co-cubes-2019/)
