<h1 align="center">Lowest Common Ancestor in a BST</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 65.2%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 176K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a Binary Search Tree (with all values unique) and two nodes <b>n1 </b>and <b>n2 </b>(n1 != n2). You may assume that both nodes exist in the tree. Find the <b>Lowest Common Ancestor (LCA)</b> of the given two nodes in the BST.

<b>LCA</b> between two nodes <b>n1 </b>and <b>n2 </b>is defined as the lowest node that has both n1 and n2 as descendants (where we allow a node to be a descendant of itself).

<b>Examples:</b>

<pre><b>Input: </b>root = [5, 4, 6, 3, N, N, 7, N, N, N, 8], n1 = 7, n2 = 8
        
<b>Output: </b>7<br><b>Explanation:</b> 7 is the closest node to both 7 and 8, which is also an ancestor of both the nodes.
</pre>

<pre><b>Input: </b>root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14], n1 = 8, n2 = 14<br>                
<b>Output: </b>8<br><b>Explanation:</b> 8 is the closest node to both 8 and 14, which is also an ancestor of both the nodes.</pre>

<pre><b>Input: </b>root = [2, 1, 3], n1 = 1, n2 = 3
        
<b>Output: </b>2<br><b>Explanation:</b> 2 is the closest node to both 1 and 3, which is also an ancestor of both the nodes.</pre>

<b>Constraints:</b><br>1 <= number of nodes <= 10<sup>5<br></sup>1 <= node->data <= 10<sup>5<br></sup>1 <= n1, n2 <= 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(h)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Tree` `Data Structures`
- **Company Tags:** `Flipkart` `Accolite` `Amazon` `Microsoft` `Samsung` `MAQ Software` `Synopsys`

### Related Articles
- [Lowest Common Ancestor In A Binary Search Tree](https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/)

### Related Interview Experiences
- [Accolite Interview Experience Set 3 On Campus](https://www.geeksforgeeks.org/accolite-interview-experience-set-3-on-campus/)
- [Samsung Rd Institute Noidasrin Internship Interview Experience](https://www.geeksforgeeks.org/samsung-rd-institute-noidasrin-internship-interview-experience/)
