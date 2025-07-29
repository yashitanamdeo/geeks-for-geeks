<h1 align="center">Topological sort</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 56.52%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 304K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>Directed Acyclic Graph (DAG)</b> of <b>V </b>(0 to V-1) vertices and <b>E</b> edges represented as a 2D list of <b>edges[][]</b>, where each entry <b>edges[i] = [u, v]</b> denotes a directed<b> </b>edge u -> v. Return the <b>topological sort</b> for the given graph.

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge <b>u </b><b>-> </b><b>v</b>, vertex <b><b>u</b></b> comes before <b><b>v</b></b> in the ordering.
<b>Note: </b>As there are multiple Topological orders possible, you may return any of them. If your returned Topological sort is correct then the output will be <b>true</b> else <b>false</b>.

<b>Examples:</b>

<pre><b>Input:</b> V = 4, E = 3, edges[][] = [[3, 0], [1, 0], [2, 0]]<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700255/Web/Other/blobid0_1744196747.jpg" alt="" title="" width="330" height="247"/><br><b>Output: </b>true<br><b>Explanation</b>: The output true denotes that the order is valid. Few valid Topological orders for the given graph are:
[3, 2, 1, 0]<br>[1, 2, 3, 0]<br>[2, 3, 1, 0]</pre>

<pre><b>Input: </b>V = 6, E = 6, edges[][] = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5,2]]<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700255/Web/Other/blobid1_1744196789.jpg" alt="" title="" width="361" height="269"/><br><b>Output: </b>true
<b>Explanation: </b>The output true denotes that the order is valid. Few valid Topological orders for the graph are:<br>[4, 5, 0, 1, 2, 3]<br>[5, 2, 4, 0, 1, 3]</pre>

<b>Constraints:</b><br>2  ≤  V  ≤  5 x 10<sup>3</sup><br>1  ≤  E = edges.size()  ≤  min[10<sup>5</sup>, (V * (V - 1)) / 2]

## Expected Complexities
- Time Complexity: O(V + E)
- Auxiliary Space: O(V)

<hr>

### Tags
- **Topic Tags:** `Graph` `Data Structures`
- **Company Tags:** `Moonfrog Labs` `Flipkart` `Morgan Stanley` `Accolite` `Amazon` `Microsoft` `OYO Rooms` `Samsung` `D-E-Shaw` `Visa`

### Related Articles
- [Topological Sorting](https://www.geeksforgeeks.org/topological-sorting/)

### Related Interview Experiences
- [De Shaw Interview Experience Off Campus 3](https://www.geeksforgeeks.org/de-shaw-interview-experience-off-campus-3/)
