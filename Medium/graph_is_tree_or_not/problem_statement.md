<h1 align="center">Graph is Tree or Not</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.18%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 39K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an undirected graph of <b>N</b> nodes (numbered from 0 to N-1) and <b>M</b> edges. Return 1 if the graph is a tree, else return 0.

<b>Note:</b> The input graph can have self-loops and multiple edges.

<b>Example 1:</b>

<pre><b>Input:</b>
N = 4, M = 3
G = [[0, 1], [1, 2], [1, 3]]
<b>Output:</b> <br>1
<b>Explanation: <br></b>Every node is reachable and the graph has no loops, so it is a tree
</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N = 4, M = 3
G = [[0, 1], [1, 2], [2, 0]]
<b>Output:</b> <br>0
<b>Explanation:</b> <br>3 is not connected to any node and there is a loop 0->1->2->0, so it is not a tree.
</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>isTree()</b> which takes the integer N (the number nodes in the input graph) and the edges representing the graph as input parameters and returns 1 if the input graph is a tree, else 0.

<b>Expected Time Complexity:</b> O(N+M)<br><b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>1 <= N <= 2*10<sup>5</sup><br>0 <= M <= 2*10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `DFS` `Graph` `Tree` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Check Given Graph Tree](https://www.geeksforgeeks.org/check-given-graph-tree/)
