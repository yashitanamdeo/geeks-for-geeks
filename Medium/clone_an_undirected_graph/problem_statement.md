<h1 align="center">Clone an Undirected Graph</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 67.49%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 40K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>connected undirected graph </b>represented by adjacency list, <b>adjList[][] </b>with <b>n </b>nodes, having a <b>distinct label </b>from <b>0 to n-1</b>, where each <b>adj[i]</b> represents the list of vertices connected to vertex i.

Create a <b>clone </b>of the graph, where each node in the graph contains an integer <b>val</b> and an array (<b>neighbors</b>) of nodes,<b> </b>containing nodes that are adjacent to the current node.

<pre>class Node {
    val: integer
    neighbors: List[Node]
}</pre>

Your task is to complete the function <b>cloneGraph( ) </b>which takes a starting node of the graph as input and returns the <b>copy of the given node</b> as a reference to the cloned graph.

<b>Note: </b>If you return a <b>correct copy </b>of the given graph, then the driver code will print <b>true</b>; and if an incorrect copy is generated or when you return the original node, the driver code will print <b>false</b>.

<b>Examples :</b>

<pre><b>Input: </b>n = 4, adjList[][] = [[1, 2], [0, 2], [0, 1, 3], [2]]
<b>Output: </b>true
<b>Explanation: <br><br></b>As the cloned graph is identical to the original one the driver code will print true.</pre>

<pre><b>Input: </b>n = 3, adjList[][] = [[1, 2], [0], [0]]
<b>Output: </b>true
<b>Explanation: <br><br></b>As the cloned graph is identical to the original one the driver code will print true.<br></pre>

<b>Constraints:</b><br>1 ≤ n ≤ 10<sup>4<br></sup>0 ≤ no. of edges ≤ 10<sup>5</sup><br>0 ≤ adjList[i][j] < n

## Expected Complexities
- Time Complexity: O(n + m)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Graph` `DFS` `BFS`
- **Company Tags:** `Google`

### Related Articles
- [Clone An Undirected Graph](https://www.geeksforgeeks.org/clone-an-undirected-graph/)
