<h1 align="center">Sum of leaf nodes in BST</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 70.36%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 49K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>Binary Search Tree </b>with <b>n</b> nodes, find the sum of all <b>leaf nodes</b>. <b>BST </b>has the following property (duplicate nodes are possible):

- The<b> left subtree </b>of a node contains only nodes with <b>keys less </b>than the node’s key.
- The<b> right subtree </b>of a node contains only nodes with<b> keys greater</b> <b>than </b>or <b>equal </b>to the node’s key.
Your task is to determine the <b>total sum </b>of the values of the <b>leaf nodes</b>.

<b>Note: </b>Input array <b>arr</b> doesn't represent the actual <b>BST</b>, it represents the order in which the elements will be added into the <b>BST</b>.

<pre><b>Example 1:</b><br><b>Input:</b><br>n = 6<br>arr = {67, 34, 82, 12, 45, 78}<br><b>Output:</b><br>135<br><b>Explanation:</b><br>In first test case, the BST for the given input will be-<br>                67<br>             /     \<br>           34       82<br>          /   \    /<br>         12   45  78<br><br>Hence, the required sum= 12 + 45 + 78 = 135<br><br><b>Example 2:</b><br><b>Input:</b><br>n = 1<br>arr = {45}<br><b>Output:</b><br>45<br><b>Explanation:<br></b>As the root node is a leaf node itself, <br>the required sum will be 45</pre>

<b>Your Task:</b><br>You don't have to take any input or print anything. You are required to complete the function <b>sumOfLeafNodes </b>that takes <b>root node of a BST </b>with <b>n</b> nodes as <b>parameter </b>and returns <b>the sum of leaf nodes</b>. 

<b>Expected Time Complexity:</b> O(n)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>1 <= n <= 10<sup>4<br></sup>1 <= Value of each node <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Data Structures`
- **Company Tags:** `None`
