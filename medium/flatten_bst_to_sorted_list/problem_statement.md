<h1 align="center">Flatten BST to sorted list</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 68.49%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 33K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a <b>Binary Search Tree (BST) </b>with <b>n</b> nodes, each node has a distinct value assigned to it. The goal is to flatten the tree such that, the <b>left child</b> of each element points to nothing <b>(NULL),</b> and the <b>right child </b>points to the next element in the sorted list of elements of the <b>BST </b>(look at the examples for clarity). You must accomplish this <b>without using any extra storage</b>, except for recursive calls, which are allowed.

<b>Note:</b> If your <b>BST </b>does have a <b>left child</b>, then the system will print a <b>-1 </b>and will skip it, resulting in an <b>incorrect solution</b>.

<b>Example 1:</b>

<pre><b>Input:</b>
          5
        /    \
       3      7
      /  \    /   \
     2   4  6     8
<b>Output: </b>2 3 4 5 6 7 8
<b>Explanation: </b>
After flattening, the tree looks
like this
    2
     \
      3
       \
        4
         \
          5
           \
            6
             \
              7
               \
                8
Here, left of each node points
to NULL and right contains the
next node.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
       5
        \
         8
       /   \
      7     9  
<b>Output:</b> 5 7 8 9
<b>Explanation:</b>
After flattening, the tree looks like this:
   5
    \
     7
      \
       8
        \
         9</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>flattenBST() </b>which takes <b>root node </b>of the <b>BST</b> as input parameter and returns the root node after transforming the tree.

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>1 <= Number of nodes <= 10<sup>3</sup><br>1 <= Data of a node <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Data Structures`
- **Company Tags:** `Adobe` `Amazon`

### Related Articles
- [Flatten Bst To Sorted List Increasing Order](https://www.geeksforgeeks.org/flatten-bst-to-sorted-list-increasing-order/)
