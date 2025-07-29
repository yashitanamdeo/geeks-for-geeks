<h1 align="center">Eventual Safe States</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 55.52%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 69K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

A directed graph of <b>V</b> vertices and <b>E</b> edges is given in the form of an adjacency list <b>adj</b>. Each node of the graph is labelled with a distinct integer in the range <b>0</b> to <b>V - 1</b>.

A node is a <b>terminal node</b> if there are no outgoing edges. A node is a <b>safe node</b> if every possible path starting from that node leads to a <b>terminal node</b>.

You have to return an array containing all the <b>safe nodes</b> of the graph. The answer should be sorted in <b>ascending</b> order.

<b>Examples</b>

<pre><b>Input:</b>
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/711095/Web/Other/blobid0_1745299307.jpg" alt="" title="" width="355" height="314"/><br><b>Output: </b>2 4 5 6
<b>Explanation:</b>
The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no 
outgoing edges from either of them. 
Every path starting at nodes 2, 4, 5, and 6 all 
lead to either node 5 or 6.
</pre>

<pre><b>Input:</b>
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/711095/Web/Other/blobid1_1745299371.jpg" alt="" title="" width="361" height="237"/><br><b>Output: </b>3
<b>Explanation:</b>
Only node 3 is a terminal node, and every path 
starting at node 3 leads to node 3.
</pre>

<b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>eventualSafeNodes</b><b>() </b>which takes an integer <b>V</b> denoting no. of vertices and <b>adj</b> denoting adjacency list of the graph and returns an array of <b>safe nodes</b>.

<b>Expected Time Complexity:</b> O(V + E)

<b>Expected Space Complexity:</b> O(V)

<b>Constraints:</b>

- 1 <= V <= 10<sup>4</sup>
- 0 <= E <= 10<sup>4</sup>
- The graph won't contain self loops.
- Each node in the graph has a distinct value in the range 0 to V - 1.


<hr>

### Tags
- **Topic Tags:** `DFS` `Graph` `BFS` `Data Structures` `Algorithms`
- **Company Tags:** `Bloomberg`

### Related Articles
- [Eventual Safe States](https://www.geeksforgeeks.org/eventual-safe-states/)
