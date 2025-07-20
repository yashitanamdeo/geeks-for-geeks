<h1 align="center">Find all Critical Connections in the Graph</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.25%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 36K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

A <b>critical connection </b>refers to an edge that, upon removal, will make it impossible for certain nodes to reach each other through any path. You are given an <b>undirected connected graph </b>with <b>v</b> vertices and <b>e</b> edges where each vertex is distinct and ranges from <b>0 to v-1</b>, and you have to find all <b>critical connections </b>in the graph. It is ensured that there is at least one such edge present.

Note: Return the connections in sorted order.

<b>Examples:</b>

<pre><b>Input:</b>
<br><b>Output: </b>
0 1
0 2
<b>Explanation</b>: 
On removing edge (0, 1), you will not be able to reach node 0 and 2 from node 1. Also, on removing edge (0, 2), you will not be able to reach node 0<br>and 1 from node 2.</pre>

<pre><b>Input:</b>
<br><b>Output:</b>
2 3
<b>Explanation</b>:
The edge between nodes 2 and 3 is the only Critical connection in the given graph.
</pre>

<b>Constraints:</b><br>1 ≤ v, e ≤ 10<sup>4<br></sup>

## Expected Complexities
- Time Complexity: O(V + E)
- Auxiliary Space: O(V)

<hr>

### Tags
- **Topic Tags:** `Graph` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Find All Critical Connections In The Graph](https://www.geeksforgeeks.org/find-all-critical-connections-in-the-graph/)

### Related Interview Experiences
- [Amazon Interview Experience On Campus For Sde 1 5](https://www.geeksforgeeks.org/amazon-interview-experience-on-campus-for-sde-1-5/)
