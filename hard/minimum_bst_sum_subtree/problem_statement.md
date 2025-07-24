<h1 align="center">Minimum BST Sum Subtree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 60.49%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 21K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>binary tree </b>and a <b>target</b>, find the number of node in the minimum sub-tree with the given sum equal to the target which is also a binary search tree.

<b>Example 1:</b>

<pre><b>Input:</b>
           13
         /    \
       5       23
      / \      / \
     N   17   N   N
         /
        16
<b>Target</b>: 38
<b>Output:</b> 3
<b>Explanation</b>: 5,17,16 is the smallest subtree
with length 3.</pre>

 

<b>Example 2:</b>

<pre><b>Input:</b>
             7
           /   \
          N    23
             /   \
            10    23
           /  \   / \
          N   17 N   N
<b>Target</b>: 73
<b>Output:</b> -1
<b>Explanation</b>: No subtree is bst for the given target.</pre>

<b>Your Task:</b>  <br>You don't need to read input or print anything. Your task is to complete the function <b>minSubtreeSumBST</b>() which takes the tree <b>root</b> and <b>target</b> as input parameters which is a <b>binary Tree </b>and returns the length of the minimum subtree having a sum equal to the target but which is a <b>binary search tree</b>.

<b>Expected Time Complexity</b>: O(N), where N is no. of nodes<br><b>Expected Space Complexity: </b>O(h), where h is the height of the tree<br><br><b>Constraints:</b><br>1 <= N <= 10^5


<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Tree` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find The Minimum Sub Tree With Target Sum In A Binary Search Tree](https://www.geeksforgeeks.org/find-the-minimum-sub-tree-with-target-sum-in-a-binary-search-tree/)
