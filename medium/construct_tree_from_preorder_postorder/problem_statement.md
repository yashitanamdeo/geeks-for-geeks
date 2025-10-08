<h1 align="center">Construct Tree from Preorder & Postorder</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 81.11%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 6K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two arrays <b>pre[] </b>and <b>post[]</b> that represent the preorder and postorder traversals of a <b>full binary tree</b>. Your task is to construct the binary tree and return its <b>root</b>.

<b>Note:</b>  Full Binary Tree is a binary tree where every node has either 0 or 2 children. The preorder and postorder traversals contain unique values, and every value present in the preorder traversal is also found in the postorder traversal.

<b>Examples:</b><br>

<pre><b>Input: </b>pre[] = [1, 2, 4, 8, 9, 5, 3, 6, 7], post[] = [8, 9, 4, 5, 2, 6, 7, 3, 1]
<b>Output: </b>[1, 2, 3, 4, 5, 6, 7, 8, 9]<b>
Explanation: </b>The tree will look like<br>   <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/912973/Web/Other/blobid0_1759763376.jpg" alt="" title="" width="211" height="187"/><br></pre>

<pre><b>Input: </b>pre[] = [1, 2, 4, 5, 3, 6, 7] , post[] = [4, 5, 2, 6, 7, 3, 1]
<b>Output: </b>[1, 2, 3, 4, 5, 6, 7]<br><b>Explanation: </b>The tree will look like<b><br></b>   <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/912973/Web/Other/blobid1_1759763386.jpg" alt="" title="" width="200" height="177"/></pre>

<b>Constraints:</b><br>1 ≤ number of nodes ≤ 10<sup>3</sup><br>1 ≤ pre[i], post[i] ≤ 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Full And Complete Binary Tree From Given Preorder And Postorder Traversals](https://www.geeksforgeeks.org/full-and-complete-binary-tree-from-given-preorder-and-postorder-traversals/)
