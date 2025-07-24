<h1 align="center">Mother Vertex</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 47.64%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 84K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a Directed Graph, find a Mother Vertex in the Graph (<b>if present</b>). <br>A Mother Vertex is a vertex through which we can reach all the other vertices of the Graph.

<b>Examples:</b>

<pre><b>Input:</b><br><br><b>Output: </b>0<br><b>Explanation: </b>According to the given edges, all 
nodes can be reached from nodes from 0, 1 and 2. 
But, since 0 is minimum among 0,1 and 2, so 0 
is the output.</pre>

<pre><b>Input:</b>
<br><b>Output: </b>-1<br><b>Explanation: </b>According to the given edges, 
no vertices are there from where we can 
reach all vertices. So, output is -1.
</pre>

<b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>findMotherVertex() </b>which takes V denoting the number of vertices and adjacency list as input parameter and returns the vertices from through which we can traverse all other vertices of the graph. If there is more than one possible nodes then return the node with minimum value. If not possible returns -1.<br><br><b>Expected Time Complexity: </b>O(V + E)<br><b>Expected Space Complexity: </b>O(V)<br><br><b>Constraints:</b><br>1 ≤ V ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `DFS` `Graph` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find A Mother Vertex In A Graph](https://www.geeksforgeeks.org/find-a-mother-vertex-in-a-graph/)
