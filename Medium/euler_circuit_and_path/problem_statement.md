<h1 align="center">Euler circuit and Path</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.89%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 41K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 25m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

<b>An Eulerian Path</b> is a path in graph that visits every edge exactly once. <b>An Eulerian Circuit </b>is <b>an Eulerian Path </b>which starts and ends on the same vertex. Given an <b>undirected graph</b> with <b>V</b> nodes, and <b>E</b> edges, with adjacency list <b>adj, </b>return 2 if the graph contains an <b>eulerian circuit</b>, else if the graph contains an <b>eulerian path, </b>return 1, otherwise, return 0.

<b>Examples</b>

<pre><b>Input: 
</b><br><b>Output: </b>2
<b>Explanation: <br></b>Following is an eulerian circuit in the mentioned graph<b><br></b>1 -> 2 -> 0 -> 1</pre>

<pre><b>Input: </b><br><br><b>Output: </b>1
<b>Explanation: <br></b>Following is an eulerian path in the mentioned graph<br>1 -> 0 -> 2</pre>

<b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>isEulerCircuilt() </b>which takes number of vertices in the graph denoted as <b>V</b> and an adjacency list of graph denoted as <b>adj </b>and returns 2 if the graph contains an <b>eulerian circuit</b>, else if the graph contains an <b>eulerian path, </b>it returns 1, otherwise, it will return 0.

<b>Expected Time Complexity: </b>O(V+E) where E is the number of edges in graph.<br><b>Expected Space Complexity: </b>O(V)

<b>Constraints:</b><br>1 ≤ V, E ≤ 10<sup>4<br></sup>1 ≤ adj[i][j] ≤ V-1<sup><br></sup>


<hr>

### Tags
- **Topic Tags:** `Graph` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Eulerian Path And Circuit](https://www.geeksforgeeks.org/eulerian-path-and-circuit/)
