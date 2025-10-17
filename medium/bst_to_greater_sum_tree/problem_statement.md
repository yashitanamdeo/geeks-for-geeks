<h1 align="center">BST to greater sum tree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 66.73%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 23K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given the <b>root </b>of a  BST with unique node values, transform it into <b>greater sum tree </b>where each node contains sum of all nodes greater than that node.

<b>Examples:</b>

<pre><b>Input: </b>root = [11, 2, 29, 1, 7, 15, 40, N, N, N, N, N, N, 35, N]<br>      <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/706357/Web/Other/blobid0_1759556071.webp" alt="" title="" width="261" height="233"/><br><b>Output:</b> [119, 137, 75, 139, 130, 104, 0, N, N, N, N, N, N, 40, N]<br><b>Explanation: </b>Every node is replaced with the sum of nodes greater than itself. <br>      <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/706357/Web/Other/blobid1_1759556181.webp" alt="" title="" width="262" height="234"/>
</pre>

<pre><b>Input</b><b>:</b> root = [2, 1, 6, N, N, 3, 7]<br>     <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/706357/Web/Other/blobid2_1759556893.webp" alt="" title="" width="276" height="212"/><br><b>Output: </b>[16, 18, 7, N, N, 13, 0]<br><b>Explanation: </b>Every node is replaced with the sum of nodes greater than itself. <br>     <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/706357/Web/Other/blobid3_1759556991.webp" alt="" title="" width="267" height="205"/></pre>

<b>Constraints :</b>
1 ≤ node->data ≤ 3*10<sup>4</sup>
1 ≤ number of nodes ≤ 3*10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Tree` `Data Structures`
- **Company Tags:** `Amazon` `Microsoft`

### Related Articles
- [Transform Bst Sum Tree](https://www.geeksforgeeks.org/transform-bst-sum-tree/)

### Related Interview Experiences
- [Amazon Interview Experience For Sde 3](https://www.geeksforgeeks.org/amazon-interview-experience-for-sde-3/)
