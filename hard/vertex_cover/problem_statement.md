<h1 align="center">Vertex Cover</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 62.97%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 27K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

<b>Vertex cover </b>of an undirected graph is a list of vertices such that every vertex not in the vertex cover shares their every edge with the vertices in the <b>vertex cover</b>. In other words, for every edge in the graph, atleast one of the endpoints of the graph should belong to the <b>vertex cover</b>. You will be given an undirected graph <b>G</b>, and your task is to determine the <b>smallest possible size </b>of a <b>vertex cover.</b>

<b>Example 1:</b>

<pre><b>Input:</b>
N=5
M=6
edges[][]={{1,2}
           {4, 1},
           {2, 4},
           {3, 4},
           {5, 2},
           {1, 3}}
<b>Output:</b>
3
<b>Explanation:</b>
{2, 3, 4} forms a vertex cover<br>with the smallest size.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N=2
M=1
edges[][]={{1,2}} <br><b>Output:</b> <br>1 <br><b>Explanation:</b> <br>Include either node 1 or node 2<br>in the vertex cover.</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Your task is to complete the function <b>vertexCover()</b> which takes the <b>edge list </b>and an integer <b>n </b>for the number of nodes of the graph<b> </b>as input parameters and returns the <b>size of the smallest possible vertex cover</b>.

<b>Expected Time Complexity:</b> O(M*2<sup>N</sup>)<br><b>Expected Auxiliary Space:</b> O(N<sup>2</sup>)<br><br> <b>Constraints:</b><br>1 <= N <= 16<br>1 <= M <= N*(N-1)/2<br>1 <= edges[i][0], edges[i][1] <= N


<hr>

### Tags
- **Topic Tags:** `None`
- **Company Tags:** `None`

### Related Articles
- [Introduction And Approximate Solution For Vertex Cover Problem](https://www.geeksforgeeks.org/introduction-and-approximate-solution-for-vertex-cover-problem/)
