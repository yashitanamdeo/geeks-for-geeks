<h1 align="center">Nodes at even distance</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 34.09%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 14K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a connected acyclic graph with n nodes and n-1 edges, count the pair of nodes that are at even distance(number of edges) from each other.

<br>
<b>Example 1:</b>

<pre><b>Input:</b>
n = 3
graph = {{}, {2}, {1, 3}, {2}}
<b>Output:</b> 1
<b>Explaination:</b> Here there are three pairs {1,2},{1,3}
and {2,3} and only {1,3} has even distance between them.
i.e           1
             /
            2
           /
          3</pre>

<br>
<b>Example 2:</b>

<pre><b>Input:</b>
n = 5
graph = {{}, {2,4}, {1,3}, {2}, {1,5}, {4}}
<b>Output:</b> 4
<b>Explaination:</b> There are four pairs {1,3},{1,5},{2,4}
and {3,5} which has even distance.
</pre>

<br>
<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>countOfNodes()</b> which takes the array <b>graph[]</b> (given as [Adjacency list](https://en.wikipedia.org/wiki/Adjacency_list#:~:text=In%20graph%20theory%20and%20computer,particular%20vertex%20in%20the%20graph.)) and its size <b>n </b>as input parameters and returns the count of pair of nodes that are at even distance from each other

<br>
<b>Expected Time Complexity:</b> O(V+E)<br>
<b>Expected Auxiliary Space:</b> O(V)

<br>
<b>Constraints:</b><br>
1 ≤ n ≤ 10<sup>4</sup>


<hr>

### Tags
- **Topic Tags:** `Graph` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Find Count Of Pair Of Nodes At Even Distance](https://www.geeksforgeeks.org/find-count-of-pair-of-nodes-at-even-distance/)
