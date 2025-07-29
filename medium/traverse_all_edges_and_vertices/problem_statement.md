<h1 align="center">Traverse All Edges And Vertices</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.34%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 31K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are presented with an <b>undirected connected graph </b>consisting of <b>n</b> vertices and connections between them represented by an <b>adjacency matrix</b>. Your objective is to determine whether it is possible to start traversing from a node, <b>x</b>, and return to it after traversing all the vertices <b>at least once</b>, using each edge <b>exactly once</b>.

<b>Example 1:</b>

<pre><b>Input: <br></b>paths = 0 1 1 1 1<br>        1 0 0 1 0<br>        1 0 0 1 0<br>        1 1 1 0 1<br>        1 0 0 1 0<br><b>Output: </b>1<br><b>Explanation: <br></b>One can visit the vertices in the following way:
1->3->4->5->1->4->2->1 (assuming 1-based indexing)
Here all the vertices has been visited and all
paths are used exactly once.<br></pre>

<b>Example 2:</b>

<pre><b>Input: <br></b>paths = 0 1 1 0<br>        1 0 1 1<br>        1 1 0 0<br>        0 1 0 0
<b>Output: </b>0
<b>Explanation: <br></b>There exists no such vertex from which all the <br>vertices could be visited and all edges are used <br>exactly once.</pre>

<b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>isPossible() </b>which takes adjacency matrix <b>paths</b> as an input parameter and returns <b>1 </b>if it is possible to start traversing from a node, <b>x</b>, and come back to it after traversing all the vertices <b>at least once</b>, using each edge <b>exactly once</b>.

 <b>Expected Time Complexity: </b>O(n<sup>2</sup>)<br><b>Expected Space Compelxity: </b>O(1)

<b>Constraints:</b><br>1 <= n <= 100<br>0 <= paths[i][j] <= 1<br><b>Note:</b> paths[i][j] = 0 where i == j or there exists no edge between i and j. paths[i][j] = 1 means there is a path between i to j.


<hr>

### Tags
- **Topic Tags:** `Graph` `Data Structures`
- **Company Tags:** `None`
