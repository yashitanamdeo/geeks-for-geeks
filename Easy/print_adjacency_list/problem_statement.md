<h1 align="center">Print adjacency list</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 43.42%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 168K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an undirected graph with <b>V </b>nodes and <b>E</b> <b>edges</b>, create and return an [adjacency list](https://www.geeksforgeeks.org/adjacency-list-meaning-definition-in-dsa/) of the graph. <b>0-based indexing</b> is followed everywhere.

<b>Example 1:</b>

<pre><b>Input:<br></b>V = 5, E = 7<br>edges = [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]
<br><b>Output:</b> 
[[1,4], [0,2,3,4], [1,3], [1,2,4], [0,1,3]]
<b>Explanation</b>:
Node 0 is connected to 1 and 4.<br>Node 1 is connected to 0,2,3 and 4.<br>Node 2 is connected to 1 and 3.<br>Node 3 is connected to 1,2 and 4.<br>Node 4 is connected to 0,1 and 3.
</pre>

<b>Example 2:</b>

<pre><b>Input:<br></b>V = 4, E = 3<br>edges = [[0,3], [0,2], [2,1]]
  <br><b>Output:</b> 
[[2,3], [2], [0,1], [0]]
<b>Explanation</b>:<br>Node 0 is connected to 2 and 3.<br>Node 1 is only connected to 2.<br>Node 2 is connected to 0 and 1.<br>Node 3 is only connected to 0.</pre>

<b>Constraints:</b><br>1 ≤ V, E ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(V + E)
- Auxiliary Space: O(V + E)

<hr>

### Tags
- **Topic Tags:** `Graph` `Data Structures`
- **Company Tags:** `None`
