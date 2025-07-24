<h1 align="center">Number of Good Components</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 60.81%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 47K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an undirected graph with <b>v </b>vertices(numbered from <b>1</b> to <b>v</b>) and <b>e </b>edges. Find the number of good components in the graph.<br>A component of the graph is good if and only if the component is fully connected.<br><b>Note: </b>A fully connected component is a subgraph of a given graph such that there's an edge between every pair of vertices in the component, the given graph can be a <b>disconnected graph. </b>

<b>Examples</b>

<pre><b>Input:</b> e=3, v=3, edges[][] = [[1, 2], [1, 3], [3, 2]]<br><br><b>Output: </b>1<b>
Explanation: <br></b>We can see that there is only one component in the graph and in this component there is a edge between any two vertces<b>.</b></pre>

<pre><b>Input:</b>e=5, v=7, edges[][] = [[1, 2] ,[7, 2], [3, 5], [3, 4], [4, 5]]
<br><b>Output: </b>2
<b>Explanation: <br></b>We can see that there are 3 components in the graph. For 1-2-7 there is no edge between 1 to 7, so it is not a fully connected component. Rest 2 are individually fully connected component.</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>findNumberOfGoodComponent()</b>, which<b> </b>takes an integer <b>e</b> and <b>v </b>and <b>edges[][] </b>as input parameters and returns an integer denoting the number of good components. 

<b>Expected Time Complexity:</b> O(v+e)<br><b>Expected Auxiliary Space:</b> O(depth of the graph)

<b>Constraints:<br></b>1 <= edges[i][0], edges[i][1] <= v<br>1 ≤ v, e ≤ 10<sup>4</sup><br>All edges are unique


<hr>

### Tags
- **Topic Tags:** `DFS` `Graph` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Counting Good Components In Undirected Graph](https://www.geeksforgeeks.org/counting-good-components-in-undirected-graph/)
