<h1 align="center">City With the Smallest Number of Neighbors at a Threshold Distance</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.12%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 60K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There are <b>n</b> cities labeled from 0 to n-1 with <b>m </b>edges connecting them. Given the array <b>edges</b> where <b>edges[i] = [from<sub>i </sub>, to<sub>i ,</sub>weight<sub>i</sub>]<sub> </sub></b> represents a <b>bidirectional </b>and <b>weighted edge </b>between cities <b>from<sub>i</sub> </b>and <b>to<sub>i</sub></b>, and given the integer <b>distanceThreshold</b>. You need to find out a city with the <b>smallest number </b>of cities that are reachable through some path and whose distance is <b>at most</b> <b>Threshold Distance.</b> If there are multiple such cities, our answer will be the city with the <b>greatest label</b>.

<b>Note:</b> The distance of a path connecting cities <i><b>i</b></i> and <i><b>j</b></i> is equal to the sum of the edge's weights along that path.

<b>Examples</b>

<pre><b>Input:</b>
n = 4, m = 4
edges = [[0, 1, 3],<br>         [1, 2, 1], <br>         [1, 3, 4],  <br>         [2, 3, 1]]
distanceThreshold = 4
<b>Output:<br></b>3
<b>Explaination:<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/711146/Web/Other/blobid1_1745300064.jpg" alt="" title="" width="278" height="278"/><br></b>The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
</pre>

<pre><b>Input: </b><br>n = 5, m = 6<br>edges = [[0, 1, 2],
         [0, 4, 8],<br>         [1, 2, 3], <br>         [1, 4, 2], <br>         [2, 3, 1],<br>         [3, 4, 1]]<br>distanceThreshold = 2.<br><b>Output:<br></b>0<br><b>Explaination:<br></b><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/711146/Web/Other/blobid2_1745300084.jpg" alt="" title="" width="320" height="320"/><br>The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.<br></pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>findCity( ) </b>which takes a number of nodes <b>n, </b>total number of edges <b>m</b> and vector of <b>edges</b> and <b>distanceThreshold</b>. and return the city with the smallest number of cities that are reachable through some path and whose distance is <b>at most</b> Threshold Distance. If there are multiple such cities, return the city with the greatest label.

<b>Expected Time Complexity: </b>O(n<sup>2</sup> + length(edges)*nlog(n) )<br><b>Expected Auxiliary Space:  </b>O(n<sup>3</sup>)

<b>Constraints:</b><br>1  ≤  n ≤  100<br>1 <= m <= n*(n-1)/2<br>length(edges[i]) == 3<br>0 <= from<sub>i </sub>< to<sub>i</sub> < n<br>1 <= weight<sub>i </sub>distanceThreshold <= 10<sup>4</sup><br>All pairs (from<sub>i</sub>, to<sub>i</sub>) are distinct


<hr>

### Tags
- **Topic Tags:** `Graph` `Shortest Path` `BFS` `Disjoint Set` `Data Structures` `Algorithms`
- **Company Tags:** `None`
