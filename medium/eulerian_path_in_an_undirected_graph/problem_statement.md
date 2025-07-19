<h1 align="center">Eulerian Path in an Undirected Graph</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 58.57%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 11K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an adjacency matrix representation of an unweighted undirected graph named <b>graph</b>, which has <b>N</b> vertices. You have to find out if there is an [eulerian path](https://en.wikipedia.org/wiki/Eulerian_path) present in the graph or not.<br><b>Note:</b> The graph consists of a single component

<b>Example 1:</b>

<pre><b>Input:</b> N = 5
graph = {{0, 1, 0, 0, 1}, 
         {1, 0, 1, 1, 0}, 
         {0, 1, 0, 1, 0}, 
         {0, 1, 1, 0, 0}, 
         {1, 0, 0, 0, 0}}
<b>Output:</b> 1
<b>Explaination:</b> There is an eulerian path. 
The path is 5->1->2->4->3->2.</pre>

<b>Example 2:</b>

<pre><b>Input:</b> N = 5
graph = {{0, 1, 0, 1, 1}, 
         {1, 0, 1, 0, 1}, 
         {0, 1, 0, 1, 1}, 
         {1, 0, 1, 0, 0}, 
         {1, 1, 1, 0, 0}}
<b>Output:</b> 0
<b>Explaination:</b> There is no eulerian path in 
the graph.</pre>

<b>Your Task:</b><br>You do not need to read input or print anything. Your task is to complete the function <b>eulerPath()</b> which takes N and graph as input parameters and returns 1 if there is an eulerian path. Otherwise returns 0.

<b>Expected Time Complexity:</b> O(N<sup>2</sup>)<br><b>Expected Auxiliary Space:</b> O(N<sup>2</sup>)

<b>Constraints:</b><br>1 ≤ N ≤ 50


<hr>

### Tags
- **Topic Tags:** `Graph` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Eulerian Path Undirected Graph](https://www.geeksforgeeks.org/eulerian-path-undirected-graph/)
