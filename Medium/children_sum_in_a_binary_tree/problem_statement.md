<h1 align="center">Children Sum in a Binary Tree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.58%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 204K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree having <b>n</b> nodes. Check whether all of its nodes have a value equal to the sum of their child nodes. Return 1 if all the nodes in the tree satisfy the given properties, else it returns 0. For every node, the data value must be equal to the sum of the data values in the left and right children. Consider the data value 0 for a NULL child. Also, leaves are considered to follow the property.

<b>Examples:</b>

<pre><b>Input:<br></b>Binary tree
       35
      /  \
     20   15
    / \   / \
   15  5 10  5

<b>Output: </b>1<b>
Explanation: <br></b>Here, every node is sum of its left and right child.</pre>

<pre><b>Input:<br></b>Binary tree
       1
     /   \
    4     3
   /  
  5    
<b>Output: </b>0<b>
Explanation: <br></b>Here, 1 is the root node and 4, 3 are its child nodes. 4 + 3 = 7 which is not equal to the value of root node. Hence, this tree does not satisfy the given condition.</pre>

<pre><b>Input:</b><br>Binary tree
       10
      /  \
     4    6
    / \  / \
   1   3 2  4
<br><b>Output: </b>1<br><b>Explanation: </b><br>Here, every node is a sum of its left and right child.</pre>

<b>Constraints:</b><br>1 <= number of nodes <= 10<sup>5</sup><br>0 <= node->data <= 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(h)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Intuit`

### Related Articles
- [Check For Children Sum Property In A Binary Tree](https://www.geeksforgeeks.org/check-for-children-sum-property-in-a-binary-tree/)
