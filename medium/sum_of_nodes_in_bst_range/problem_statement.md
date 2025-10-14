<h1 align="center">Sum of Nodes in BST Range</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 85.12%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 7K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given the <b>root </b>of a Binary Search Tree and two integers <b>l </b>and <b>r</b>, the task is to find the <b>sum of all nodes</b> that lie between l and r, including both l and r.

<b>Examples</b>

<pre><b>Input:</b> root = [22, 12, 30, 8, 20], l = 10, r = 22<br>     <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/913091/Web/Other/blobid0_1760093593.jpg" alt="" title="" width="232" height="206"/><br><b>Output: </b>54<br><b>Explanation: </b>The nodes in the given Tree that lies in the range [10, 22] are {12, 20, 22}. Therefore, the sum of nodes is 12 + 20 + 22 = 54.</pre>

<pre><b>Input: </b>root =<b> </b>[8, 5, 11, 3, 6, N, 20], l = 11, r = 15  <br>     <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/913091/Web/Other/blobid1_1760093611.jpg" alt="" title="" width="228" height="205"/>
<b>Output: </b>11<br><b>Explanation: </b>The nodes in the given Tree that lies in the range [11, 15] is {11}. Therefore, the sum of node is 11.</pre>

<b>Constraints:</b><br>0 ≤ number of nodes ≤ 10<sup>4</sup><sup><br></sup>0 ≤ node->data ≤ 10<sup>4</sup><sup><br></sup>0 ≤ l ≤ r ≤ 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(h)

<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Sum Of Nodes In A Binary Search Tree With Values From A Given Range](https://www.geeksforgeeks.org/sum-of-nodes-in-a-binary-search-tree-with-values-from-a-given-range/)
