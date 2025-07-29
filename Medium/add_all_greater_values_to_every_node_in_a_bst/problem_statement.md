<h1 align="center">Add all greater values to every node in a BST</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 59.39%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 35K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a BST, modify it so that all greater values in the given BST are added to every node.

<b>Example 1:</b>

<pre><b>Input:</b>
           50
         /    \
        30    70
      /  \     / \  
     20  40 60 80<b>
Output: </b>350 330 300 260 210 150 80<b>
Explanation:</b>The tree should be modified to
following:
             260
          /       \
        330      150
       /   \      /     \
    350   300 210    80
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
          2
        /   \
       1     5
            /  \
           4    7<b>
Output: </b>19 18 16 12 7</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>modify() </b>which takes one argument: the root of the BST. The function should contain the logic to modify the BST so that in the modified BST, every node has a value equal to the sum of its value in the original BST and values of all the elements larger than it in the original BST. Return the root of the modified BST. The driver code will print the inorder traversal of the returned BST/<br><br><b>Expected Time Complexity: </b>O(N)<br><b>Expected Auxiliary Space: </b>O(Height of the BST).

<b>Constraints:</b><br>1<=N<=100000

<br><b>Note:</b> The <b>Input/Output</b> format and <b>Example</b> is given are used for the system's internal purpose, and should be used by a user for <b>Expected Output</b> only. As it is a function problem, hence a user should not read any input from the stdin/console. The task is to complete the function specified, and not to write the full code.


<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Tree` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Add Greater Values Every Node Given Bst](https://www.geeksforgeeks.org/add-greater-values-every-node-given-bst/)
