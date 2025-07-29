<h1 align="center">BST Maximum Difference</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 52.54%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 25K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a Binary Search Tree and a target value. You must find the maximum difference between the sum of node data from root to target and from target to a child leaf node (target exclusive). Initially, you are at the <b>root </b>node.<br><b>Note: </b>If the target node is not present in the tree then return -1.

<b>Example 1:</b>

<pre><b>Input:</b>
<img src="https://media.geeksforgeeks.org/img-practice/BSTDownwardTraversal-1662975635.png" alt="" title=""/>

Target = 20
<b>Output:</b> 10
<b>Explanation:</b> From root to target the sum of node data is 25 and from target to the children leaf nodes the sums of the node data are 15 and 22. So, the maximum difference will be (25-15) = 10.
</pre>

<b>Example 2:</b>

<pre><b>Input:
</b><img src="https://media.geeksforgeeks.org/img-practice/BSTDownwardTraversal-1662975635.png" alt="" title=""/>
Target = 50
<b>Output:</b> -1
<b>Explanation:</b> The target node is not present in the tree.
</pre>

<br><b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function maxDifferenceBST() which takes BST(you are given the root node of the BST ) and target as input, and returns an interger value as the required answer. If the target is not present in the BST then return -1.

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(H), H - Height of the Tree.

<br><b>Constraints:</b><br>1 <= n < 10^4<br>1 <= node.data < 10^5<br>1 <= target < 10^5


<hr>

### Tags
- **Topic Tags:** `DFS` `Binary Search Tree` `Data Structures` `Algorithms`
- **Company Tags:** `None`
