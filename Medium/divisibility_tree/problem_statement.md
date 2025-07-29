<h1 align="center">Divisibility tree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 68.8%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 23K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a tree with n nodes where <b>n</b> is <b>even</b>. The tree is numbered from 1 to n, has n - 1 edges and is rooted at node 1. Your task is to eliminate the <b>maximum </b>number of edges resulting in a set of disjoint trees where the number of nodes in each tree is divisible by <b>2</b>.

<b>Examples:</b>

<pre><b>Input: </b>n = 10, edges = [[2,1],[3,1],[4,3],[5,2],[6,1],[7,2],[8,6],[9,8],[10,8]]
<b>Output: </b>2
<b>Explanation:<br></b>Original tree:<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/880846/Web/Other/blobid0_1732601788.png" alt="" title="" width="432" height="428"/><br>After removing edge 1-3 and 1-6, each remaining component consists of even number of nodes. <br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/880846/Web/Other/blobid1_1732601873.png" alt="" title="" width="430" height="426"/><br></pre>

<pre><b>Input: </b>n = 4, edges = [[2,1],[4,2],[1,3]]
<b>Output: </b>1
<b>Explanation: <br></b>Original tree:<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/880846/Web/Other/blobid2_1732602037.png" alt="" title="" width="424" height="420"/><b><br></b>After removing 1-2, each remaining component consists of even number of nodes.<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/880846/Web/Other/blobid3_1732602310.png" alt="" title="" width="421" height="417"/><br></pre>

<b>Constraints:</b><br>1 <= n <= 10<sup>5</sup><br>edges.size() = n - 1<br>1 <= edges[i][0], edges[i][1] <= n

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `DFS` `Graph` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Maximum Edge Removal Tree Make Even Forest](https://www.geeksforgeeks.org/maximum-edge-removal-tree-make-even-forest/)
