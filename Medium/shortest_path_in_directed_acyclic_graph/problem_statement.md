<h1 align="center">Shortest path in Directed Acyclic Graph</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 48.48%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 184K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a Directed Acyclic Graph of V vertices from 0 to n-1 and a 2D Integer array(or vector) edges[ ][ ] of length E, where there is a directed edge from edge[i][0] to edge[i][1] with a distance of edge[i][2] for all i.

Find the <b>shortest</b> path from <b>src(0) </b>vertex to all the vertices and if it is impossible to reach any vertex, then return <b>-1</b> for that vertex.

<b>Examples :<br></b>

<pre><b>Input: </b>V = 4, E = 2, edges = [[0,1,2], [0,2,1]]
<b>Output: </b>[0, 2, 1, -1]<br><b>Explanation: </b>Shortest path from 0 to 1 is 0->1 with edge weight 2. Shortest path from 0 to 2 is 0->2 with edge weight 1. There is no way we can reach 3, so it's -1 for 3.</pre>

<pre><b>Input: </b>V = 6, E = 7, edges = [[0,1,2], [0,4,1], [4,5,4], [4,2,2], [1,2,3], [2,3,6], [5,3,1]]
<b>Output: </b>[0, 2, 3, 6, 1, 5]<br><b>Explanation: </b>Shortest path from 0 to 1 is 0->1 with edge weight 2. Shortest path from 0 to 2 is 0->4->2 with edge weight 1+2=3. Shortest path from 0 to 3 is 0->4->5->3 with edge weight 1+4+1=6. Shortest path from 0 to 4 is 0->4 with edge weight 1.Shortest path from 0 to 5 is 0->4->5 with edge weight 1+4=5.</pre>

<b>Constraint:<br></b>1 <= V <= 100<br>1 <= E <= min((N*(N-1))/2,4000)<br>0 <= edges<sub>i,0</sub>, edges<sub>i,1</sub> < n<br>0 <= edge<sub>i,2</sub> <=10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n + m)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Graph` `Shortest Path` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Shortest Path For Directed Acyclic Graphs](https://www.geeksforgeeks.org/shortest-path-for-directed-acyclic-graphs/)
