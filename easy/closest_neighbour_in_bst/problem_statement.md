<h1 align="center">Closest Neighbour in BST</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 36.98%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 63K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given the <b>root</b> of a<b> [binary search tree](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)</b> and a number <b>k</b>, find the greatest number in the binary search tree that is less than or equal to <b>k</b>.

Note: "If no such node value exists that is smaller than <i>k</i>, then return -1."

<b>Examples:</b>

<pre><b>Input: </b>root = [10, 7, 15, 2, 8, 11, 16], k = 14<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/895571/Web/Other/blobid3_1747652897.jpg" alt="" title="" width="250" height="195"/><br><b>Output:</b> 11
<b>Explanation:</b> The greatest element in the tree which is less than or equal to 14, is 11.</pre>

<pre><b>Input: </b>root = [5, 2, 12, 1, 3, 9, 21, N, N, N, N, N, N, 19, 25], k = 24<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/895571/Web/Other/blobid0_1747652607.jpg" alt="" title="" width="288" height="251"/><br><b>Output:</b> 21
<b>Explanation:</b> The greatest element in the tree which is less than or equal to 24, is 21. <br></pre>

<pre><b>Input:</b> root = [5, 2, 12, 1, 3, 9, 21, N, N, N, N, N, N, 19, 25], k = 4<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/895571/Web/Other/blobid2_1747652761.jpg" alt="" title="" width="281" height="244"/><br><b>Output:</b> 3
<b>Explanation:</b> The greatest element in the tree which is less than or equal to 4, is 3.<br></pre>

<b>Constraints:</b><br>1 <= number of nodes <= 10<sup>5<br></sup>1 <= node->data, k <= 10<sup>5<br></sup>All nodes are unique in the BST

## Expected Complexities
- Time Complexity: O(h)
- Auxiliary Space: O(h)

<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Tree` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Largest Number Bst Less Equal N](https://www.geeksforgeeks.org/largest-number-bst-less-equal-n/)
