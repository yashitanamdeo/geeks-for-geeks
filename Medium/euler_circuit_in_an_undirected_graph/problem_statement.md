<h1 align="center">Euler Circuit in an Undirected Graph</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.88%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 35K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 25m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

<b>[Eulerian Path](https://en.wikipedia.org/wiki/Eulerian_path) </b>is a path in a graph that visits <b>every edge exactly once</b>. Eulerian Circuit is an Eulerian Path that <b>starts</b> and <b>ends</b> on the <b>same vertex</b>. Given the number of vertices <b>v</b> and adjacency list <b>adj</b> denoting the graph. Find that there exists the Euler circuit or not. Return <b>1</b> if there exist  <b>alteast one</b> eulerian circuit else <b>0.</b>

<b>Examples</b>

<pre><b>Input: </b>v = 4, edges[][] = [[0, 1], [0, 2], [1, 3], [2, 3]]
 <br><b>Output: </b>1
<b>Explanation: </b>corresponding adjacency list will be {{1, 2},{0, 3},{0, 3},{1, 2}}<br>One of the Eularian circuit 
starting from vertex 0 is as follows:
0->1->3->2->0
</pre>

<pre><b>Input: </b>v = 3, edges[][] = [[0, 1], [0, 2]]    
<br><b>Output: </b>0<br><b>Explanation: </b>corresponding adjacency list will be {{1, 2}}<b><br></b>No Eulerian path is found.</pre>

<b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>isEularCircuitExist()</b> which takes <b>v</b> and array of edges <b>adj[]</b> as input parameter and returns boolean value <b>1</b> if Eular circuit exists otherwise returns <b>0</b>.

<b>Expected Time Complexity: </b>O(v + e)<br><b>Expected Space Complexity: </b>O(v)

<b>Constraints:</b><br>1 <= v <= 10<sup>5</sup><br>1 <= edges <= 2*10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `DFS` `Graph` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Euler Circuit Directed Graph](https://www.geeksforgeeks.org/euler-circuit-directed-graph/)
- [Eulerian Path And Circuit](https://www.geeksforgeeks.org/eulerian-path-and-circuit/)
