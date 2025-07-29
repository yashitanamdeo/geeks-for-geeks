<h1 align="center">Flatten binary tree to linked list</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 75.82%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 45K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given the root of a binary tree, flatten the tree into a "Linked list":

- The "linked list" should use the same Node class where the right child pointer points to the next node in the list and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.
<b>Examples:</b>

<pre><b>Input: </b>
          1
        /   \
       2     5
      / \     \
     3   4     6<br><b>Output : </b>1 2 3 4 5 6 <br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/706436/Web/Other/blobid0_1722839451.png" alt="" title="" height="100"/> <br><b>Explanation: </b>After flattening, the tree looks like this - <br>     1
      \
       2
        \
         3
          \
           4
            \ 
             5 <br>              \<br>               6<br>Here, left of each node points to NULL and right contains the next node in preorder.The inorder traversal of this flattened tree is 1 2 3 4 5 6.<br><br><b>Input :</b>
        1
       / \
      3   4
         /
        2
         \
          5 
<b>Output :</b> 
1 3 4 2 5 
<b>Explanation : </b>After flattening, the tree looks like this -
     1
      \
       3
        \
         4
          \
           2
            \ 
             5 
Here, left of each node points to NULL and right contains the next node in preorder.The inorder traversal of this flattened tree is 1 3 4 2 5.</pre>

<b>Expected Time Complexity: </b>O(n)
<b>Expected Space </b><b>Complexity</b><b>:</b> O(1)
 
<b>Constraints :</b>
1<= number of nodes in binary tree <= 10<sup>5</sup>
1<= data of nodes <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Linked List` `Tree` `Data Structures`
- **Company Tags:** `Microsoft`

### Related Articles
- [Flatten A Binary Tree Into Linked List](https://www.geeksforgeeks.org/flatten-a-binary-tree-into-linked-list/)
