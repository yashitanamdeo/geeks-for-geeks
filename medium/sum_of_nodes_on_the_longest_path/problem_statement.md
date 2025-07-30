<h1 align="center">Sum of nodes on the longest path</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 52.39%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 125K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree <b>root[]</b>, you need to find the <b>sum </b>of the nodes on the <b>longest path</b> from the <b>root </b>to any <b>leaf node</b>. If two or more paths have the same length, the path with the <b>maximum </b>sum of node values should be considered.

<b>Examples:</b>

<pre><b>Input:</b> root[] = [4, 2, 5, 7, 1, 2, 3, N, N, 6, N]<br> <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700680/Web/Other/blobid0_1733503356.jpg" alt="" title="" width="288" height="257"/>
<b>Output:</b> 13
<b>Explanation:</b>
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700680/Web/Other/blobid1_1733503411.jpg" alt="" title="" width="294" height="263"/><br>The highlighted nodes <b>(4, 2, 1, 6)</b> above are part of the longest root to leaf path having sum = (4 + 2 + 1 + 6) = 13</pre>

<pre><b>Input: </b>root[] = [1, 2, 3, 4, 5, 6, 7]<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/895566/Web/Other/blobid0_1747478981.jpg" alt="" title="" width="292" height="226"/><br><b>Output: </b>11<br><b>Explanation: <br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/895566/Web/Other/blobid1_1747479038.jpg" alt="" title="" width="292" height="226"/><br></b>The longest root-to-leaf path is 1 -> 3 -> 7, with sum 11.</pre>

<pre><b>Input: </b>root[] = [10, 5, 15, 3, 7, N, 20, 1]<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/895566/Web/Other/blobid2_1747479147.jpg" alt="" title="" width="292" height="254"/><br><b>Output: </b>19<br><b>Explanation: <br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/895566/Web/Other/blobid3_1747479244.jpg" alt="" title="" width="291" height="253"/><br></b>The longest root-to-leaf path is 10 -> 5 -> 3 -> 1 with a sum of 10 + 5 + 3 + 1 = 19.</pre>

<b>Constraints:</b><br>1 <= number of nodes <= 10<sup>6</sup><br>0 <= node->data <= 10<sup>4</sup><br>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Traversal` `Tree` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Sum Nodes Longest Path Root Leaf Node](https://www.geeksforgeeks.org/sum-nodes-longest-path-root-leaf-node/)
