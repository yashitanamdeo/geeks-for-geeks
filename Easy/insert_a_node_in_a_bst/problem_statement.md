<h1 align="center">Insert a node in a BST</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 47.15%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 172K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>BST</b>(Binary Search Tree) and a key <b>key</b>. If the key is not present in the BST, Insert a new node with a value equal to the key into the BST. If the key is already present in the BST, don't modify the BST. Return the root of the modified BST after inserting the key. 

<b>Note: </b>The generated output contains the in-order traversal of the modified tree.

<b>Examples :</b>

<pre><b>Input: </b>key = 4
<br><b>Output: </b>1 2 3 4<b>
Explanation: </b>After inserting the node 4 Inorder traversal will be 1 2 3 4.
</pre>

<pre><b>Input: </b>key = 4<br> <br><b>Output: </b>1 2 3 4 6<b>
Explanation: </b>After inserting the node 4 Inorder traversal of the above tree will be 1 2 3 4 6.<br></pre>

<pre><b>Input: </b>key = 2
<b><br>Output: </b>1 2 3 <b>
Explanation:</b> Node with key=2 already present in BST, Inorder traversal will be 1 2 3.</pre>

<b>Constraints:</b><br>1 <= number of nodes <= 10<sup>5<br></sup>1 <= node->data <= 10<sup>9</sup><br>1 <= key <= 10<sup>9</sup>

## Expected Complexities
- Time Complexity: O(h)
- Auxiliary Space: O(h)

<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Design-Pattern` `Data Structures`
- **Company Tags:** `Paytm` `Accolite` `Amazon` `Microsoft` `Samsung`

### Related Articles
- [Binary Search Tree Set 1 Search And Insertion](https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/)
