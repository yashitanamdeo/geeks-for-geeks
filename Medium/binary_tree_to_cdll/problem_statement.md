<h1 align="center">Binary Tree to CDLL</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 71.66%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 55K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 45m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree (BT), the task is to convert this to a Circular Doubly Linked List (CDLL) in-place. The<b> </b>left and right pointers<b> </b>in nodes will be used as previous and next pointers<b> </b>respectively in CDLL. The order of nodes in CDLL<b> </b>must be the same as <b>Inorder </b>of the given <b>Binary Tree</b>. The first node of <b>Inorder traversal </b>(leftmost node in<b> </b>BT) must be the<b> </b>head node of the CDLL.

<b>Examples:</b>

<pre><b>Input:
</b>      1
    /   \
   3     2
<b>Output:
</b>3 1 2 
2 1 3<br><b>
Explanation: </b>After converting tree to CDLL when CDLL is is traversed from head to tail and then tail to head, elements are displayed as in the output.
</pre>

<pre><b>Input:
</b>     10
   /    \
  20    30
 /  \
40  60
<b>Output:
</b>40 20 60 10 30 
30 10 60 20 40<br><b>
Explanation: </b>After converting tree to CDLL, when CDLL is is traversed from head totail and then tail to head, elements are displayed as in the output.</pre>

<b>Constraints:<br></b>1 <= number of nodes <= 10<sup>3<br></sup>0 <= data of a node <= 10<sup>4</sup>

<b>Expected Time Complexity: </b>O(n)<br><b>Expected Space C</b><b>omplexity</b><b>: </b>O(h) , where h = height of tree


<hr>

### Tags
- **Topic Tags:** `Linked List` `Tree` `Data Structures`
- **Company Tags:** `Amazon` `SAP Labs`

### Related Articles
- [Convert A Binary Tree To A Circular Doubly Link List](https://www.geeksforgeeks.org/convert-a-binary-tree-to-a-circular-doubly-link-list/)
