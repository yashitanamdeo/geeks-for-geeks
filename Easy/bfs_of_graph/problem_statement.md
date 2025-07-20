<h1 align="center">BFS of graph</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 44.09%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 502K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 10m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>connected undirected graph</b> containing<b> V </b>vertices, represented by a 2-d adjacency list <b>adj[][]</b>, where each adj[i] represents the list of vertices connected to vertex i. Perform a <b>Breadth First Search (BFS) </b>traversal starting from vertex 0, visiting vertices from left to right according to the given adjacency list, and return a list containing the BFS traversal of the graph.

<b>Note:</b> Do traverse in the <b>same order</b> as they are in the given <b>adjacency list</b>.

<b>Examples:</b>

<pre><b>Input: </b>adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]<br><br><b>Output:</b> [0, 2, 3, 1, 4]<br><b>Explanation:</b> Starting from 0, the BFS traversal will follow these steps: <br>Visit 0 → Output: 0 <br>Visit 2 (first neighbor of 0) → Output: 0, 2 <br>Visit 3 (next neighbor of 0) → Output: 0, 2, 3 <br>Visit 1 (next neighbor of 0) → Output: 0, 2, 3, <br>Visit 4 (neighbor of 2) → Final Output: 0, 2, 3, 1, 4</pre>

<pre><b>Input: </b>adj[][] = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]<br><br><b>Output:</b> [0, 1, 2, 3, 4]<br><b>Explanation: </b>Starting from 0, the BFS traversal proceeds as follows: <br>Visit 0 → Output: 0 <br>Visit 1 (the first neighbor of 0) → Output: 0, 1 <br>Visit 2 (the next neighbor of 0) → Output: 0, 1, 2 <br>Visit 3 (the first neighbor of 2 that hasn't been visited yet) → Output: 0, 1, 2, 3 <br>Visit 4 (the next neighbor of 2) → Final Output: 0, 1, 2, 3, 4</pre>

<b>Constraints:<br></b>1 ≤ V = adj.size() ≤ 10<sup>4<br></sup>1 ≤ adj[i][j] ≤ 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(V + E)
- Auxiliary Space: O(V + E)

<hr>

### Tags
- **Topic Tags:** `Graph` `BFS` `Data Structures` `Algorithms`
- **Company Tags:** `Flipkart` `Amazon` `Microsoft` `Samsung` `Ola Cabs` `Adobe` `SAP Labs`

### Related Articles
- [Breadth First Search Or Bfs For A Graph](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)

### Related Interview Experiences
- [Adobe Interview Experience Set 48 Campus](https://www.geeksforgeeks.org/adobe-interview-experience-set-48-campus/)
