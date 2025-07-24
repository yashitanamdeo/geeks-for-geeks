<h1 align="center">Articulation Point - I</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 39.26%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 80K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an undirected connected graph with <b>V </b>vertices and adjacency list <b>adj</b>. You are required to find all the vertices removing which (and edges through it) disconnects the graph into 2 or more components and return it in sorted manner.<br><b>Note: </b>Indexing is zero-based i.e nodes numbering from (0 to V-1). There might be loops present in the graph.

<b>Example 1:</b>

<pre><b>Input:
</b>
<b>Output:</b>{1,4}
<b>Explanation: </b>Removing the vertex 1 will
discconect the graph as-

Removing the vertex 4 will disconnect the
graph as-

</pre>

 

<b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>articulationPoints</b><b>() </b>which takes V and adj as input parameters and returns a list containing all the vertices removing which turn the graph into two or more disconnected components in sorted order. If there are no such vertices then returns a list containing -1.<br> 

<b>Expected Time Complexity: </b>O(V + E)<br><b>Expected Auxiliary Space: </b>O(V)<br> 

<b>Constraints:</b><br>1 ≤ V ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Graph` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Articulation Points Or Cut Vertices In A Graph](https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/)
