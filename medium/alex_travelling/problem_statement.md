<h1 align="center">Alex Travelling</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 61.59%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 14K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Alex is very fond of traveling. There are <b>n </b>cities, labeled from<b> 1</b> to<b> n</b>.  You are also given flights, a list of travel flights as <b>directed weighted</b> edges<b> flights[i] = (u<sub>i</sub>,v<sub>i</sub>,w<sub>i</sub>)</b> where<b> u<sub>i </sub></b>is the source node,<b> v<sub>i</sub> </b>is the target node, and <b>w<sub>i</sub></b> is the price it takes for a person to travel from source to target.<br>Currently, Alex is in <b>k</b>'th city and wants to visit one city of his choice. Return the<b> minimum </b>money Alex should have so that he can visit any city of his choice from <b>k</b>'th city. If there is a city that has no path from <b>k</b>'th city, which means Alex can't visit that city, return <b>-1</b>. <br>Alex always takes the optimal path. He can any city via another city by taking multiple flights.<br> 

<b>Examples</b>

<pre><b>Input:</b>
n: 4
k: 2
flights size: 3
flights: [[2,1,1],[2,3,1],[3,4,1]]
<b>Output:</b>
2
<b>Explanation:</b>
to visit 1 from 2 takes cost 1
to visit 2 from 2 takes cost 0
to visit 3 from 2 takes cost 1
to visit 4 from 2 takes cost 2,
2->3->4
So if Alex wants to visit city 4
from 2, he needs 2 units of money
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/711152/Web/Other/blobid0_1750669077.webp" alt="" title="" width="245" height="275"/>  </pre>

<pre><b>Input:</b>
n: 4 
k: 3 
flights size: 3 
flights: [[2,1,1],[2,3,1],[3,4,1]] 
<b>Output:</b> -1
<b>Explanation:</b>
There is no direct or indirect path 
to visit city 2 and 1 from city 3
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/711152/Web/Other/blobid1_1750669108.webp" alt="" title="" width="200" height="224"/>  </pre>

<b>Your Task:</b>

You don't need to print or input anything. Complete the function <b>minimumCost() </b>which takes a  flights array, an integer n and an integer k<b> </b>as the input parameters and returns an integer, denoting the<b> minimum </b>money Alex should have so that he can visit any city of his choice from k'th city.<br><br><b>Expected Time Complexity:</b> O((V+E) log V), here V is number of cities and E is number of flights. <br><b>Expected Auxiliary Space</b>: O(V+E), here V is number of cities and E is number of flights. 

<b>Constraints:</b>

- 2 <= n <= 500
- 1 <= flights.length <= 100000
- flights[i].length == 3
- 1 <= u<sub>i</sub>, v<sub>i</sub>, k<= n
- u<sub>i</sub> != v<sub>i</sub>
- 1 <= w<sub>i</sub> <= 100
- All the pairs (u<sub>i</sub>, v<sub>i</sub>) are <b>unique</b>. (i.e., no multiple edges)


<hr>

### Tags
- **Topic Tags:** `Graph` `Data Structures`
- **Company Tags:** `None`
