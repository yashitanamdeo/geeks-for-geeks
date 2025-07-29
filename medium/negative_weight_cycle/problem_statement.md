<h1 align="center">Negative weight cycle</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 41.9%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 73K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a weighted directed graph with n nodes and m edges. Nodes are labeled from 0 to n-1, the task is to check if it contains a negative weight cycle or not.<br><b>Note: </b>edges[i] is defined as u, v and weight.<br> 

<b>Example 1:</b>

<pre><b>Input: </b>n = 3, edges = {{0,1,-1},{1,2,-2},
{2,0,-3}}
<b>Output: </b>1
<b>Explanation: </b>The graph contains negative weight
cycle as 0->1->2->0 with weight -1,-2,-3.
</pre>

<b>Example 2:</b>

<pre><b>Input: </b>n = 3, edges = {{0,1,-1},{1,2,-2},
{2,0,3}}
<b>Output: </b>0
<b>Explanation: </b>The graph does not contain any
negative weight cycle.
</pre>

 

<b>Your Task:</b><br>You don't need to read or print anyhting. Your task is to complete the function <b>isNegativeWeightCycle() </b>which takes n and edges as input paramater and returns 1 if graph contains negative weight cycle otherwise returns 0.<br> 

<b>Expected Time Complexity: </b>O(n*m)<br><b>Expected Space Compelxity: </b>O(n)<br> 

<b>Constraints:</b><br>1 <= n <= 100<br>0 <= m <= n*(n-1), where m is the total number of Edges in the directed graph.


<hr>

### Tags
- **Topic Tags:** `Graph` `Data Structures`
- **Company Tags:** `Cisco`

### Related Articles
- [Detect Negative Cycle Graph Bellman Ford](https://www.geeksforgeeks.org/detect-negative-cycle-graph-bellman-ford/)
