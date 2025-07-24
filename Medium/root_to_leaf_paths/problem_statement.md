<h1 align="center">Root to Leaf Paths</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 43.65%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 152K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>Binary Tree</b>, you need to <b>find all the possible paths</b> from the <b>root node</b> to all the <b>leaf nodes</b> of the binary tree. 

<b>Note:</b> The paths should be returned such that paths from the left subtree of any node are <b>listed first</b>, followed by paths from the right subtree.

<b>Examples:</b>

<pre><b>Input: </b>root[] = [1, 2, 3, 4, 5, N, N]

<b>Output: </b>[[1, 2, 4], [1, 2, 5], [1, 3]]
<b>Explanation: </b>All the possible paths from root node to leaf nodes are: 1 -> 2 -> 4, 1 -> 2 -> 5 and 1 -> 3</pre>

<pre><b>Input: </b>root[] = [1, 2, 3]<br><br><b>Output: </b>[[1, 2], [1, 3]] 
<b>Explanation: </b>All the possible paths from root node to leaf nodes are: 1 -> 2 and 1 -> 3
</pre>

<pre><b>Input:</b> root[] = [10, 20, 30, 40, 60, N, N]
<b><br>Output: </b>[[10, 20, 40], [10, 20, 60], [10, 30]]<br><b>Explanation: </b>All the possible paths from root node to leaf nodes are: 10 -> 20 -> 40, 10 -> 20 -> 60 and 10 -> 30</pre>

<b>Constraints:</b><br>1 <= number of nodes <= 10<sup>4<br></sup>1 <= node->data <= 10<sup>4</sup><sup><br></sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(h)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures` `Recursion` `Arrays` `Binary Search Tree`
- **Company Tags:** `Paytm` `Amazon`

### Related Articles
- [Given A Binary Tree Print All Root To Leaf Paths](https://www.geeksforgeeks.org/given-a-binary-tree-print-all-root-to-leaf-paths/)

### Related Interview Experiences
- [Amazon Interview Experience Set 323 Software Development Engineer Off Campus](https://www.geeksforgeeks.org/amazon-interview-experience-set-323-software-development-engineer-off-campus/)
