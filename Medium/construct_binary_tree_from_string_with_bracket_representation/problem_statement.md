<h1 align="center">Construct Binary Tree from String with bracket representation</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 59.15%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 24K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Construct a binary tree from a string consisting of parenthesis and integers. The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the roots value and a pair of parenthesis contains a child binary tree with the same structure. Always start to construct the left child node of the parent first if it exists. The integer values will be less than or equal to 10^5.

<b>Example 1:</b>

<pre><b>Input:</b> "1(2)(3)" 
<b>Output:</b> 2 1 3
<b>Explanation:</b>
           1
          / \
         2   3
Explanation: first pair of parenthesis contains 
left subtree and second one contains the right 
subtree. Inorder of above tree is "2 1 3".</pre>

<b>Example 2:</b>

<pre><b>Input:</b> "4(2(3)(1))(6(5))"
<b>Output:</b> 3 2 1 4 5 6
<b>Explanation:</b>
           4
         /   \
        2     6
       / \   / 
      3   1 5   </pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>treeFromString() </b>which takes a string <b>str </b>as input parameter and returns the root node of the tree.

<br><b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(N)

<br><b>Constraints:</b><br>1 <= |str| <= 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Strings` `Tree` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Construct Binary Tree String Bracket Representation](https://www.geeksforgeeks.org/construct-binary-tree-string-bracket-representation/)
