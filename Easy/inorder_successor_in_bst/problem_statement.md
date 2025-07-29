<h1 align="center">Inorder Successor in BST</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 34.97%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 141K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a BST, and a reference to a Node <b>k</b> in the BST. Find the Inorder Successor of the given node in the BST. If there is no successor, return -1. 

<b>Examples :</b>

<pre><b>Input:</b> root = [2, 1, 3], k = 2
   <b> </b>  2
    /   \
<b>   </b>1     3
<b>Output: </b>3 
<b>Explanation:</b> Inorder traversal : 1 2 3 Hence, inorder successor of 2 is 3.
</pre>

<pre><b>Input:</b> root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14], k = 8
             20
            /   \
           8<b>     </b>22
          / \
         4   12
            /<b>  </b>\
           10   14
<b>Output: </b>10<b>
Explanation: </b>Inorder traversal: 4 8 10 12 14 20 22. Hence, successor of 8 is 10.<br></pre>

<pre><b>Input:</b> root = [2, 1, 3], k = 3
      2
    /   \
<b>   </b>1     3
<b>Output: </b>-1 
<b>Explanation:</b> Inorder traversal : 1 2 3 Hence, inorder successor of 3 is null.</pre>

<b>Constraints:</b><br>1 <= n <= 10<sup>5</sup><sup>,</sup> where n is the number of nodes

## Expected Complexities
- Time Complexity: O(Height of the BST)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Data Structures`
- **Company Tags:** `Morgan Stanley` `Amazon` `Microsoft`

### Related Articles
- [Inorder Successor In Binary Search Tree](https://www.geeksforgeeks.org/inorder-successor-in-binary-search-tree/)

### Related Interview Experiences
- [Amazon Interview Experience Set 350 Sde](https://www.geeksforgeeks.org/amazon-interview-experience-set-350-sde/)
