<h1 align="center">Median of BST</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 27.43%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 106K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given the <b>root </b>of a Binary Search Tree, find the median of it. 

Let the nodes of the BST, when written in ascending order (inorder traversal), be represented as V1, V2, V3, …, Vn, where n is the total number of nodes in the BST.

- If number of nodes are even: return <b>V(n/2)</b>
- If number of nodes are odd: return <b>V((n+1)/2)</b>
<b>Examples:</b>

<pre><b>Input: </b>root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14]
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20251007111944537098/2.webp" alt="2" title="" width="271" height="333"/><b>
Output: </b>12
<b>Explanation: </b>The inorder of given BST is 4, 8, 10, 12, 14, 20, 22. Here, n = 7, so, here median will be ((7+1)/2)th value, i.e., 4th value, i.e, 12.</pre>

<pre><b>Input: </b>root = [5, 4, 8, 1]
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20251007111944589768/1.webp" alt="1" title="" width="281" height="247"/> <b>
Output: </b>4<b>
Explanation: </b>The inorder of given BST is 1, 4, 5, 8. Here, n = 4(even), so, here median will be (4/2)th value, i.e., 2nd value, i.e, 4.</pre>

<b>Constraints:</b><br>1 ≤ number of nodes ≤ 10<sup>5<br></sup>1 ≤ node.data ≤  10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Traversal` `Binary Search Tree` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon`

### Related Articles
- [Find Median Bst Time O1 Space](https://www.geeksforgeeks.org/find-median-bst-time-o1-space/)
