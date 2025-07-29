<h1 align="center">Transitive closure of a Graph</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 29.1%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 52K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a directed graph, determine whether a vertex <b>j</b> is reachable from another vertex <b>i</b> for all vertex pairs <b>(i, j)</b> in the given <b>graph</b>. Here, vertex <b>j</b> is reachable from another vertex <b>i </b>means that there is a path from vertex <b>i </b>to <b>j.</b> The reachability matrix is called the <b>transitive closure of a graph</b>. The directed graph is represented by an <b>adjacency matrix </b>where there are <b>N</b> vertices. 

<b>Example 1:</b>

<pre><b>Input:</b> N = 4
graph = {{1, 1, 0, 1}, 
         {0, 1, 1, 0}, 
         {0, 0, 1, 1}, 
         {0, 0, 0, 1}}
<b>Output:</b> {{1, 1, 1, 1}, 
         {0, 1, 1, 1}, 
         {0, 0, 1, 1}, 
         {0, 0, 0, 1}}
<b>Explanation: <br></b>The output list shows the reachable indexes.<br></pre>

<b>Example 2:</b>

<pre><b>Input:</b> N = 3
graph = {{1, 0, 0}, 
         {0, 1, 0}, 
         {0, 0, 1}}
<b>Output:</b> {{1, 0, 0}, 
         {0, 1, 0}, 
         {0, 0, 1}}
<b>Explanation: <br></b>The output list shows the reachable indexes.</pre>

<b>Your Task:</b><br>You do not need to read input or print anything. Your task is to complete the function <b>transitiveClosure()</b> which takes an integer <b>N</b> and a 2D array <b>graph</b>(adjacency matrix of the graph)<b> </b>as <b>input parameters </b>and returns the <b>transitive closure </b>of the graph in the form of <b>2D array</b>.

<b>Expected Time Complexity:</b> O(N<sup>3</sup>)<br><b>Expected Auxiliary Space:</b> O(N<sup>2</sup>)

<b>Constraints:</b><br>1 ≤ N ≤ 100


<hr>

### Tags
- **Topic Tags:** `Graph` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Transitive Closure Of A Graph](https://www.geeksforgeeks.org/transitive-closure-of-a-graph/)
