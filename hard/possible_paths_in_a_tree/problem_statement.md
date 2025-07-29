<h1 align="center">Possible Paths in a Tree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 71.75%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 27K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>weighted</b> tree with <b>n</b> nodes and (<b>n-1</b>) edges. You are given <b>q</b> <b>queries</b>. Each query contains a number <b>x</b>. For each query, find the number of paths in which the maximum edge weight is less than or equal to <b>x</b>. 

<b>Note:</b> Path from A to B and B to A are considered to be the same.

<b>Example 1:</b>

<pre><b>Input:</b> <br>n = 3
edges {start, end, weight} = {{1, 2, 1}, {2, 3, 4}}
q = 1
queries[] = {3}
<b>Output:</b> <br>1
<b>Explanation:</b>
Query 1: Path from 1 to 2</pre>

<b>Example 2:</b>

<pre><b>Input:</b> <br>n = 7
edges {start, end, weight} = {{1, 2, 3}, {2, 3, 1}, {2, 4, 9}, {3, 6, 7}, {3, 5, 8}, {5, 7, 4}}
q = 3
queries[] = {1, 3, 5}
<b>Output:</b> <br>1 3 4
<b>Explanation:</b> 
Query 1: Path from 2 to 3
Query 2: Path from 1 to 2, 1 to 3, and 2 to 3
Query 3: Path from 1 to 2, 1 to 3, 2 to 3, and 5 to 7
</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Complete the function <b>maximumWeight()</b>which takes integers <b>n,</b> list of <b>edges</b> where each edge is given by {start,end,weight}, an integer <b>q </b>and a list of q <b>queries</b> as input parameters and returns a list of integers denoting the number of possible paths for each query. 

<b>Expected Time Complexity: </b>O(nlogn + qlogn)<br><b>Expected Auxiliary Space: </b>O(n)

<b>Constraints:</b><br>2 ≤ n ≤ 10<sup>4<br></sup>1 ≤ q ≤ 10<sup>4</sup><sup><br></sup>1 ≤ edges[i][0], edges[i][1] ≤ n<br>edges[i][0] != edges[i][1]<br>0 ≤ edges[i][2] ≤ 10<sup>5</sup><br>0 ≤ queries[i] ≤ 10<sup>5</sup><br>


<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures` `union-find`
- **Company Tags:** `None`
