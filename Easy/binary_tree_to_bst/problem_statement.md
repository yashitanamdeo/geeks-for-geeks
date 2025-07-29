<h1 align="center">Binary Tree to BST</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 60.75%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 80K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a Binary Tree, convert it to Binary Search Tree in such a way <b>that keeps the original structure of Binary Tree intact</b>.<br> <b>Example 1:</b>

<pre><b>Input:
      </b>1
    /   \
<b>   </b>2     3<b>
Output: <br></b>1 2 3<br><b>Explanation:</b><br>The converted BST will be <br>      2<br>    /   \<br>   1     3</pre>

<br><b>Example 2:</b>

<pre><b>Input:
</b>          1
       /    \
     2       3
   /        
 4       <b>
Output: <br></b>1 2 3 4<b>
Explanation:
</b>The converted BST will be

        3
      /   \
    2     4
  /
 1
</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>binaryTreeToBST()</b> which takes the root of the Binary tree as input and returns the root of the BST. The driver code will print<b> inorder</b> traversal of the converted BST.

<b>Expected Time Complexity:</b> O(NLogN).<br><b>Expected Auxiliary Space:</b> O(N).

<b>Constraints:</b><br>1 <= Number of nodes <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Tree` `Data Structures`
- **Company Tags:** `Amazon` `Adobe`

### Related Articles
- [Binary Tree To Binary Search Tree Conversion](https://www.geeksforgeeks.org/binary-tree-to-binary-search-tree-conversion/)
