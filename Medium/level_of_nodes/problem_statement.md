<h1 align="center">Level of Nodes</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.95%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 61K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an integer <b>x</b> and an undirected acyclic graph with <b>v nodes</b>, labeled from <b>0 </b>to <b>v-1</b>, and <b>e </b>edges, return the <b>level </b>of node labeled as <b>x</b>.

<b>Level </b>is the <b>minimum </b>number of edges you must travel from the node 0 to some target.

If there doesn't exists such a node that is labeled as <b>x</b>, <b>return -1</b>.<br>

<b>Examples :</b>

<pre><b>Input: </b><b>x</b> = 4
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/701248/Web/Other/blobid0_1745299763.jpg" alt="" title="" width="414" height="366"/><br><b>Output: </b>2
<b>Explanation</b>:
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/701248/Web/Other/blobid1_1745299817.jpg" alt="" title="" width="461" height="307"/><br>We can clearly see that Node 4 lies at Level 2.
</pre>

<pre><b>Input: </b><b>x</b> = 1
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/701248/Web/Other/blobid2_1745299852.jpg" alt="" title="" width="314" height="209"/> <br><b>Output: </b>1
<b>Explanation</b>: Node 1 lies at level 1, immediate after Node 0.</pre>

<b>Expected Time Complexity: </b>O(v)<br><b>Expected Auxiliary Space: </b>O(v)

<b>Constraints:</b><br>2  ≤ v ≤  10<sup>4<br></sup>1 ≤ e ≤ 10<sup>4</sup><br>0  ≤ adj<sub>i, j</sub> < v<br>1  ≤ x < v<br>

<b>Note : </b>Graph doesn't contain multiple edges and self loops.


<hr>

### Tags
- **Topic Tags:** `Graph` `BFS` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find The Level Of Given Node In An Undirected Graph](https://www.geeksforgeeks.org/find-the-level-of-given-node-in-an-undirected-graph/)
