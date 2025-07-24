<h1 align="center">AVL Tree Insertion</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 37.01%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 45K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an AVL tree and N values to be inserted in the tree. Write a function to insert elements into the given <b>AVL tree</b>.

<b>Note:</b><br>The tree will be checked after each insertion. <br>If it violates the properties of balanced BST, an error message will be printed followed by the inorder traversal of the tree at that moment.<br>If instead all insertions are successful, inorder traversal of the tree will be printed.

<b>Example 1:</b>

<pre><b>Input:<br></b>N = 3<b><br></b>Values to be inserted = {5,1,4}<b> </b>
<b>Output:<br></b>1 4 5<br><b>Explanation:<br></b>Value to be inserted = 5<b><br></b>    5
Value to be inserted = 1
    5
   /
  1
Value to be inserted = 4
  5                     4
 /    <b>LR rotation</b>        /  \
1    ----------->       1   5
 \
 4<br>Therefore the inorder of the final tree will be 1, 4, 5.</pre>

<b>Example 2:</b>

<pre><b>Input:</b><br>N = 7<b><br></b>Values to be inserted = {21,26,30,9,4,14,28}<b> </b>
<b>Output:<br></b>4 9 14 21 26 28 30<br><b>Explanation:</b><br>Value to be inserted = 21<b><br></b>    21
Value to be inserted = 26
    21
     \
     26
Value to be inserted = 30
  21                        26
   \      <b>LL rotation</b>         /  \
   26    ----------->       21  30
    \
     30<br>Value to be inserted = 9<br>    26<br>   /  \<br>  21  30<br> /<br>9<br>Value to be inserted = 4<br>      26                          26<br>     /  \                          /  \<br>    21  30                      9   30<br>   /          <b>RR rotation</b>        /  \<br>  9          ----------->       4  21<br> /<br>4<br>Value to be inserted = 14<br>      26                          21<br>     /  \                          /  \<br>    9   30                      9   26<br>   / \          <b>LR rotation</b>      /  \    \<br>  4  21        ----------->    4  14  30<br>     /<br>    14<br>Value to be inserted = 28<br>      21                          21<br>     /  \                          /  \<br>    9   26                      9   28<br>   / \    \     <b>RL rotation</b>       / \    / \<br>  4  14   30   ----------->   4  14 26 30<br>          /<br>         28<br>Therefore the inorder of the final tree will be 4, 9, 14, 21, 26, 28, 30.</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Complete the function<b> insertToAVL()</b> which takes the root of the tree and the value of the node to be inserted as input parameters and returns the root of the modified tree.

<b>Expected Time Complexity:</b> O(log N)<br><b>Expected Auxiliary Space: </b>O(height of tree)

<b>Constraints:</b><br>1 ≤ N ≤ 2000


<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Tree` `Data Structures`
- **Company Tags:** `Morgan Stanley` `Amazon` `Snapdeal` `MakeMyTrip` `Oracle` `Oxigen Wallet` `Informatica` `Citicorp`

### Related Articles
- [Avl Tree Set 1 Insertion](https://www.geeksforgeeks.org/avl-tree-set-1-insertion/)
