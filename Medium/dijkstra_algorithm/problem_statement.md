<h1 align="center">Dijkstra Algorithm</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.83%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 241K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 25m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an undirected, weighted graph with <b>V </b>vertices numbered from 0 to V-1 and <b>E </b>edges, represented by 2d array <b>edges[][]</b>, where edges[i]=[u, v, w] represents the <b>edge</b> between the nodes u and v having w <b>edge weight</b>.<br>You have to find the <b>shortest distance </b>of all the vertices from the source vertex <b>src</b>, and return an array of integers where the <b>ith</b> element denotes the shortest distance between <b>ith</b> node and source vertex<b> src</b>.

<b>Note: </b>The Graph is connected and doesn't contain any negative weight edge.

<b>Examples:</b>

<pre><b>Input: </b>V = 3, edges[][] = [[0, 1, 1], [1, 2, 3], [0, 2, 6]], src = 2
<b>Output: </b>[4, 3, 0]
<b>Explanation</b>:
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/892538/Web/Other/blobid0_1744201836.jpg" alt="" title="" width="317" height="236"/><br>Shortest Paths:
For 2 to 0 minimum distance will be 4. By following path 2 -> 1 -> 0
For 2 to 1 minimum distance will be 3. By following path 2 -> 1
For 2 to 2 minimum distance will be 0. By following path 2 -> 2<br></pre>

<pre><b>Input: </b>V = 5, edges[][] = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]], src = 0
<b>Output: </b>[0, 4, 8, 10, 10]
<b>Explanation</b>: <br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/892538/Web/Other/blobid1_1744202046.jpg" alt="" title="" width="336" height="273"/><br>Shortest Paths: <br>For 0 to 1 minimum distance will be 4. By following path 0 -> 1
For 0 to 2 minimum distance will be 8. By following path 0 -> 2
For 0 to 3 minimum distance will be 10. By following path 0 -> 2 -> 3 
For 0 to 4 minimum distance will be 10. By following path 0 -> 1 -> 4</pre>

<b>Constraints:</b><br>1 ≤ V ≤ 10<sup>5</sup>
1 ≤ E = edges.size() ≤ 10<sup>5</sup><br>0 ≤ edges[i][j] ≤ 10<sup>4</sup>
0 ≤ src < V

## Expected Complexities
- Time Complexity: O((V + E) log V)
- Auxiliary Space: O(V)

<hr>

### Tags
- **Topic Tags:** `Graph` `Data Structures` `Algorithms`
- **Company Tags:** `Flipkart` `Microsoft`

### Related Articles
- [Dijkstras Shortest Path Algorithm Greedy Algo 7](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
- [Dijkstras Shortest Path Algorithm Using Set In Stl](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-using-set-in-stl/)

### Related Interview Experiences
- [Flipkart Interview Experience For Sde](https://www.geeksforgeeks.org/flipkart-interview-experience-for-sde/)
