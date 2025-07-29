<h1 align="center">Pairs violating the BST property</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 56.99%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 32K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree with <b>n</b> nodes, find the number of <b>pairs violating the BST property</b>.<br>BST has the following properties:-

- Every node is greater than its left child and less than its right child.
- Every node is greater than the maximum value of in its left subtree and less than the minimum value in its right subtree.
- The maximum in the left sub-tree must be less than the minimum in the right subtree.
<b>Example 1:</b>

<pre><b>Input : </b>
n = 5
Input tree
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/861883/Web/Other/blobid0_1709054479.png" alt="" title="" width="351" height="245"/>    
<b>Output :</b>
5
<b>Explanation : </b>
Pairs violating BST property are:-
(10,50), 10 should be greater than its left child value.
(40,30), 40 should be less than its right child value.
(50,20), (50,30) and (50,40), maximum of left subtree of 10 is 50 greater than 20, 30 and 40 of its right subtree.</pre>

<b>Example 2:</b>

<pre><b>Input : </b>
n = 6<br>Input tree
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/861883/Web/Other/blobid1_1709055216.png" alt="" title="" width="402" height="219"/>
<b>Output :</b>
9
<b>Explanation :</b>
There are total 9 pairs { (80,30),(80,60),(80,70),(30,60),(40,70),(40,30),(70,30),(70,60),(70,70) } which violate the BST properties.</pre>

<b>Your task :</b>
You don't have to read input or print anything. Your task is to complete the function <b>pairsViolatingBST</b><b>()</b> that takes the root of the tree and <b>n</b> as input and returns number of pairs violating BST property.<br>
 
<b>Expected Time Complexity: </b>O(n*logn)
<b>Expected Space Complexity: </b>O(n)
 
<b>Your Task :</b>
1 <= n <= 2*10<sup>4</sup>
-10<sup>9</sup> <= node->data <= 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Merge Sort` `Traversal` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Count Of Pairs Violating Bst Property](https://www.geeksforgeeks.org/count-of-pairs-violating-bst-property/)
