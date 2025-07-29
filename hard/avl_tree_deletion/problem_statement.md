<h1 align="center">AVL Tree Deletion</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 47.98%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 41K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an <b>AVL tree</b> and <b>N</b> values to be deleted from the tree. Write a function to delete a given value from the tree. All the <b>N</b> values which needs to be deleted are passed one by one as input <b>data </b>by driver code itself, you are asked to return the root of modified tree after deleting the value.

<pre><b>Example 1:
</b>
Tree = 
        4
      /   \
     2     6
    / \   / \  
   1   3 5   7

N = 4
Values to be deleted = {4,1,3,6}

<b>Input: </b>Value to be deleted = 4
<b>Output:</b>
        5    
      /   \
     2     6
    / \     \  
   1   3     7

<b>Input: </b>Value to be deleted = 1
<b>Output:</b>
        5    
      /   \
     2     6
      \     \  
       3     7

<b>Input: </b>Value to be deleted = 3
<b>Output:</b>
        5    
      /   \
     2     6
            \  
             7

<b>Input: </b>Value to be deleted = 6
<b>Output:</b>
        5    
      /   \
     2     7

</pre>

<b>Your Task:  </b><br>You dont need to read input or print anything. Complete the function<b> delelteNode()</b> which takes the root of the tree and the value of the node to be deleted as input parameters and returns the root of the modified tree.

<b>Note: </b>The tree will be checked after each deletion. <br>If it violates the properties of balanced BST, an error message will be printed followed by the inorder traversal of the tree at that moment.<br>If instead all deletion are successful, inorder traversal of tree will be printed.<br>If every single node is deleted from tree, 'null' will be printed.

<b>Expected Time Complexity:</b> O(height of tree)<br><b>Expected Auxiliary Space: </b>O(height of tree)

<b>Constraints:</b><br>1 ≤ N ≤ 500


<hr>

### Tags
- **Topic Tags:** `Tree` `AVL-Tree` `Data Structures` `Advanced Data Structure`
- **Company Tags:** `Morgan Stanley` `Amazon` `Snapdeal` `MakeMyTrip` `Oracle` `Oxigen Wallet`

### Related Articles
- [Deletion In An Avl Tree](https://www.geeksforgeeks.org/deletion-in-an-avl-tree/)
