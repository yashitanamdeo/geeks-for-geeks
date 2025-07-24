<h1 align="center">Construct a Full Binary Tree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 74.63%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 19K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two arrays that represent Preorder traversals of a Full binary tree <b>preOrder[]</b> and its mirror tree <b>preOrderMirror[]</b>, your task is to complete the function <b>constructBinaryTree()</b>, that constructs the full binary tree using these two Preorder traversals.

<b>N</b><b>ote</b>: It is not possible to construct a general binary tree using these two traversal. But it is possible to create a full binary tree using the above traversals without any ambiguity.

<b>Example 1:</b>

<pre><b>Input :</b>
preOrder[] = {0,1,2}
preOrderMirror[] = {0,2,1} 

<b>Output :</b>
                0
              /   \
             1     2<br><b>Explanation :<br></b>Tree in the output and it's mirror tree matches the preOrder and preOrderMirror.</pre>

<b>Example 2:</b>

<pre><b>Input :</b>  
preOrder[] = {1,2,4,5,3,6,7}
preOrderMirror[] = {1,3,7,6,2,5,4}

<b>Output :  </b>        
                 1
               /    \
              2      3
            /   \   /  \
           4     5 6    7<br><b>Explanation :<br></b>Tree in the output and it's mirror tree matches the preOrder and preOrderMirror.</pre>

<b>Your Task:</b>

You don't need to read, input, or print anything. Your task is to complete the function <b>constructBTree</b><b>, </b>The function takes three arguments as input, first the array that represent Preorder traversals of a Full binary tree <b>preOrder[], </b>second the array that represents the preorder traversal of<b> </b>its mirror tree <b>preOrderMirror[] </b>and last the <b>size</b> of both the array,and returns root of the full binary tree.

<b>Expected Time Complexity:</b> O(N^2)<br><b>Expected Auxiliary Space:</b> O(N), where N indicates number of nodes.

<b>Constraints:</b><br>1 <= Number of Nodes <= 10<sup>3</sup>


<hr>

### Tags
- **Topic Tags:** `Traversal` `Tree` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Construct Full Binary Tree Using Preorder Traversal Preorder Traversal Mirror Tree](https://www.geeksforgeeks.org/construct-full-binary-tree-using-preorder-traversal-preorder-traversal-mirror-tree/)
