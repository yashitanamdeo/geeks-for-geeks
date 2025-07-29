<h1 align="center">Kth Ancestor in a Tree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 35.06%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 125K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree of size  <b>n</b>, a <b>node,</b> and a positive integer <b>k</b>., Your task is to complete the function <b>kthAncestor()</b>, the function should return the <b>kth</b> ancestor of the given node in the binary tree. If there does not exist any such ancestor then return -1.<br><b>Note</b>: <br>1. It is guaranteed that the <b>node</b> exists in the tree.<br>2. All the nodes of the tree have distinct values.

<b>Examples :</b>

<pre><b>Input: </b>k = 2, node = 4<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700682/Web/Other/blobid0_1745302099.jpg" alt="" title="" width="268" height="237"/><br><b>Output:</b> 1
<b>Explanation:</b>
Since, k is 2 and node is 4, so we first need to locate the node and look k times its ancestors. Here in this Case node 4 has 1 as his 2nd Ancestor aka the root of the tree.</pre>

<pre><b>Input: </b>k=1, node=3    <br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700682/Web/Other/blobid1_1745302119.jpg" alt="" title="" width="271" height="240"/>
<b>Output: </b>1
<b>Explanation: </b>k=1 and node=3 ,kth ancestor of node 3 is 1.</pre>

<b>Constraints:</b><br>1<=n<=10<sup>5</sup><sup><br></sup>1<= k <= 100<br>1 <= Node.data <= n

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Google` `Facebook` `Amazon`

### Related Articles
- [Kth Ancestor Node Binary Tree](https://www.geeksforgeeks.org/kth-ancestor-node-binary-tree/)
