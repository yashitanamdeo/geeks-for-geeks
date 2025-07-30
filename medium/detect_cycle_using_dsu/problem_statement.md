<h1 align="center">Detect Cycle using DSU</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 48.37%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 65K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an <b>undirected graph</b> with <b>no self loops</b> with <b>V (from 0 to V-1)</b> nodes and <b>E</b> edges, the task is to check if there is any <b>cycle </b>in the <b>undirected graph</b>.

<b>Note:</b> Solve the problem using <b>disjoint set union (DSU).</b>

<b>Examples</b>

<pre><b>Input: 
</b><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/701410/Web/Other/blobid0_1745299580.jpg" alt="" title="" width="303" height="268"/><br><b>Output:</b><b> </b>1
<b>Explanation: </b>There is a cycle between 0->2->4->0
</pre>

<pre><b>Input: 
</b><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/701410/Web/Other/blobid1_1745299616.jpg" alt="" title="" width="307" height="272"/><br><b>Output: </b>0
<b>Explanation: </b>The graph doesn't contain any cycle
</pre>

<b>Your Task:</b><br>You don't need to read or print anyhting. Your task is to complete the function <b>detectCycle() </b>which takes number of vertices in the graph denoting as <b>V</b> and adjacency list <b>adj </b>and returns <b>1</b> if graph contains any <b>cycle </b>otherwise returns <b>0</b>.

<b>Expected Time Complexity:</b> O(V + E)<br><b>Expected Space Complexity: </b>O(V)

<b>Constraints:<br></b>2 ≤ V ≤ 10<sup>4<br></sup>1 ≤ E ≤ 10<sup>4</sup>


<hr>

### Tags
- **Topic Tags:** `Graph` `Disjoint Set` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Detect Cycle In Graph Using Dsu](https://www.geeksforgeeks.org/detect-cycle-in-graph-using-dsu/)
