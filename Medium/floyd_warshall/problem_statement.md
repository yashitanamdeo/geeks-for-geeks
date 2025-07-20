<h1 align="center">Floyd Warshall</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 32.89%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 209K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an weighted<b> directed</b> graph, represented by an adjacency matrix, <b>dist[][] </b>of size <b>n x n</b>, where <b>dist[i][j] </b>represents the weight of the edge from <b>node i to node j</b>. If there is no direct edge, <b>dist[i][j] </b>is set to a large value (i.e., <b>10<sup>8</sup></b>) to represent infinity.<br>The graph may contain <b>negative edge weights</b>, but it does not contain any <b>negative weight cycles</b>.

Your task is to find the <b>shortest distance</b> between every pair of nodes <b>i </b>and<b> j</b> in the graph.

Note: Modify the distances for every pair <b>in place</b>.

<b>Examples :</b>

<pre><b>Input: </b>dist[][] = [[0, 4, 10<sup>8</sup>, 5, 10<sup>8</sup>], [10<sup>8</sup>, 0, 1, 10<sup>8</sup>, 6], [2, 10<sup>8</sup>, 0, 3, 10<sup>8</sup>], [10<sup>8</sup>, 10<sup>8</sup>, 1, 0, 2], [1, 10<sup>8</sup>, 10<sup>8</sup>, 4, 0]]<br><br><b>Output: </b>[[0, 4, 5, 5, 7], [3, 0, 1, 4, 6], [2, 6, 0, 3, 5], [3, 7, 1, 0, 2], [1, 5, 5, 4, 0]]
<br><b>Explanation: </b>Each cell dist[i][j] in the output shows the shortest distance from node i to node j, computed by considering all possible intermediate nodes. 
</pre>

<pre><b>Input: </b>dist[][] = [[0, -1, 2], [1, 0, 10<sup>8</sup>], [3, 1, 0]]
<br><b>Output: </b>[[0, -1, 2], [1, 0, 3], [2, 1, 0]]
<br><b>Explanation: </b>Each cell dist[i][j] in the output shows the shortest distance from node i to node j, computed by considering all possible intermediate nodes.<br>From 2 to 0 shortest distance should be 2 by following path 2 -> 1 -> 0<br>From 1 to 2 shortest distance should be 3 by following path 1 -> 0 -> 2</pre>

<b>Constraints:</b><br>1 ≤ dist.size() ≤ 100<br>-1000 ≤ dist[i][j] ≤ 1000<br>dist[i][j] can be <b>10<sup>8</sup></b> to represent infinity.

## Expected Complexities
- Time Complexity: O(n^3)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Graph` `Data Structures` `Algorithms`
- **Company Tags:** `Samsung`

### Related Articles
- [Floyd Warshall Algorithm Dp 16](https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/)
