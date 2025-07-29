<h1 align="center">DFS of Graph</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 63.07%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 357K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 5m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>connected undirected graph </b>containing <b>V </b>vertices represented by a 2-d adjacency list <b>adj[][]</b>, where each adj[i] represents the list of vertices connected to vertex i. Perform a <b>Depth First Search (DFS)</b> traversal starting from vertex 0, visiting vertices from left to right as per the given adjacency list, and return a list containing the DFS traversal of the graph.

<b>Note:</b> Do traverse in the <b>same order</b> as they are in the given <b>adjacency list</b>.

<b>Examples:</b>

<pre><b>Input: </b>adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700203/Web/Other/blobid0_1728647807.jpg" alt="" title="" width="301" height="189"/><br><b>Output:</b> [0, 2, 4, 3, 1]<br><b>Explanation</b>: Starting from 0, the DFS traversal proceeds as follows:<br>Visit 0 → Output: 0 <br>Visit 2 (the first neighbor of 0) → Output: 0, 2 <br>Visit 4 (the first neighbor of 2) → Output: 0, 2, 4 <br>Backtrack to 2, then backtrack to 0, and visit 3 → Output: 0, 2, 4, 3 <br>Finally, backtrack to 0 and visit 1 → Final Output: 0, 2, 4, 3, 1</pre>

<pre><b>Input:</b> adj[][] = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700203/Web/Other/blobid1_1728648013.jpg" alt="" title="" width="300" height="189"/><br><b>Output:</b> [0, 1, 2, 3, 4]
<b>Explanation</b>: Starting from 0, the DFS traversal proceeds as follows: <br>Visit 0 → Output: 0 <br>Visit 1 (the first neighbor of 0) → Output: 0, 1 <br>Visit 2 (the first neighbor of 1) → Output: 0, 1, 2 <br>Visit 3 (the first neighbor of 2) → Output: 0, 1, 2, 3 <br>Backtrack to 2 and visit 4 → Final Output: 0, 1, 2, 3, 4</pre>

<b>Constraints:</b><br>1 ≤ V = adj.size() ≤ 10<sup>4<br></sup>1 ≤ adj[i][j] ≤ 10<sup>4</sup><sup><br></sup>

## Expected Complexities
- Time Complexity: O(V + E)
- Auxiliary Space: O(V + E)

<hr>

### Tags
- **Topic Tags:** `DFS` `Graph` `Data Structures` `Algorithms`
- **Company Tags:** `Accolite` `Amazon` `Samsung` `Intuit`

### Related Articles
- [Depth First Search Or Dfs For A Graph](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)
