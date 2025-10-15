<h1 align="center">Distribute Candies</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 63.24%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 35K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given the <b>root</b> of a binary tree with <b>n</b> nodes, where each node contains a certain number of candies, and the total number of candies across all nodes is <b>n</b>. In one move, you can select any two <b>adjacent </b>nodes and transfer one candy from one node to the other. The transfer can occur between a parent and child in <b>either </b>direction.

The task is to determine the <b>minimum </b>number of moves required to ensure that every node in the tree has <b>exactly</b> <b>one </b>candy.

<b>Note:</b> The testcases are framed such that it is always possible to achieve a configuration in which every node has exactly one candy, after some moves.

<b>Examples:</b>

<pre><b>Input</b>: root = [5, 0, 0, N, N, 0, 0]<br>  <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/912840/Web/Other/blobid0_1759751405.jpg" alt="" title="" width="287" height="177"/><br><b>Output: </b>6<br><b>Explanation</b>:<br>Move 1 candy from root to left child
Move 1 candy from root to right child
Move 1 candy from right child to root->right->left node
Move 1 candy from root to right child
Move 1 candy from right child to root->right->right node
Move 1 candy from root to right child<br>so, total 6 moves required.</pre>

<pre><b>Input</b>: root = [2, 0, 0, N, N, 3, 0]<br>  <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/912840/Web/Other/blobid1_1759751720.jpg" alt="" title="" width="281" height="173"/><br><b>Output: </b>4<br><b>Explanation</b>:<br>Move 1 candy from root to left child
Move 1 candy from root->right->left node to root->right node
Move 1 candy from root->right node to root->right->right node
Move 1 candy from root->right->left node to root->right node<br>so, total 4 moves required.</pre>

<b>Constraints:<br></b>1 ≤ n ≤ 3*10<sup>3</sup><sup><br></sup>0 ≤ Node->data ≤ n<br>The sum of all Node->data = n

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(h)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Microsoft`

### Related Articles
- [Distribute Candies In A Binary Tree](https://www.geeksforgeeks.org/distribute-candies-in-a-binary-tree/)
