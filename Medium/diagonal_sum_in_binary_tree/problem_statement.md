<h1 align="center">Diagonal sum in binary tree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 61.89%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 49K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Consider Red lines of slope -1 passing between nodes (in the following diagram). The diagonal sum in a binary tree is the sum of all node data lying between these lines. Given a Binary Tree of size <b>n</b>, print all diagonal sums.

For the following input tree, the output should be 9, 19, 42.<br>9 is the sum of 1, 3, and 5.<br>19 is the sum of 2, 6, 4, and 7.<br>42 is the sum of 9, 10, 11, and 12.

[](https://media.geeksforgeeks.org/wp-content/uploads/diagonal-sum-in-a-tree.jpg)

<b>Example 1:</b>

<pre><b>Input:</b>
         4
       /   \
      1     3
           /
          3<b>
Output: <br></b>7 4 
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
           10
         /    \
        8      2
       / \    /
      3   5  2<b>
Output: <br></b>12 15 3 
</pre>

<b>Your Task:</b><br>You don't need to take input. Just complete the function<b> diagonalSum() </b>that takes the root <b>node</b> of the tree as a parameter and returns an array containing the diagonal sums for every diagonal present in the tree with slope -1.

<b>Expected Time Complexity</b>: O(nlogn).<br><b>Expected Auxiliary Space: </b>O(n).

<b>Constraints:</b><br>1 <= n <= 10<sup>5</sup><br>0 <= data of each node <= 10<sup>4</sup>


<hr>

### Tags
- **Topic Tags:** `Recursion` `Tree` `Data Structures` `Algorithms`
- **Company Tags:** `Accolite` `Amazon`

### Related Articles
- [Diagonal Sum Binary Tree](https://www.geeksforgeeks.org/diagonal-sum-binary-tree/)
