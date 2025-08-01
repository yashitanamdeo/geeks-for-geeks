<h1 align="center">Distribute candies in a binary tree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 63.24%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 30K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a binary tree with <b>n</b> nodes, where each node contains a certain number of candies, and the total number of candies across all nodes is <b>n</b>. In one move, we can select two <b>adjacent </b>nodes and transfer one candy from one node to the other. The transfer can occur between a parent and child in <b>either </b>direction.

The task is to determine the <b>minimum </b>number of moves required to ensure that every node in the tree has <b>exactly</b> <b>one </b>candy.

<b>Note:</b> The testcases are framed such that it is always possible to achieve a configuration in which every node has exactly one candy, after some moves.

<b>Examples:</b>

<pre><b>Input</b>: root[] = [3, 0, 0]<br>       <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/706446/Web/Other/blobid0_1737544183.jpg" alt="" title="" width="210" height="186"/> <br><b>Output: </b>2<br><b>Explanation</b>: From the root of the tree, we move one candy to its left child, and one candy to its right child. </pre>

<pre><b>Input</b>: root[] = [0, 3, 0]<br>       <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/706446/Web/Other/blobid1_1737544324.jpg" alt="" title="" width="201" height="178"/>  <br><b>Output: </b>3<br><b>Explanation</b>: From the left child of the root, we move two candies to the root [taking two moves]. Then, we move one candy from the root of the tree to the right child.</pre>

<b>Constraints:</b>
1 <= n <= 10<sup>4<br></sup>0 <= Node->data <= n<br>The sum of all Node->data is equal to n

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(h)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Microsoft`

### Related Articles
- [Distribute Candies In A Binary Tree](https://www.geeksforgeeks.org/distribute-candies-in-a-binary-tree/)
