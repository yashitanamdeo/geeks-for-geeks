<h1 align="center">BST with Dead End</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 35.99%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 96K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a Binary Search Tree (BST) containing unique positive integers greater than 0.

Your task is to determine whether the BST contains a <b>dead end</b>.

<b>Note:</b> A <b>dead end</b> is a <b>leaf node</b> in the BST such that no new node can be inserted in the BST at or below this node while maintaining the BST property and the constraint that<b> </b>all node values must be > 0.

<b>Examples:</b>

<pre><b>Input: </b>root[] = [8, 5, 9, 2, 7, N, N, 1]<br><b><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700425/Web/Other/blobid1_1748007119.webp" alt="" title="" width="190" height="184"/></b><br><b>Output: </b>true
<b>Explanation: </b>Node 1 is a Dead End in the given BST.</pre>

<pre><b>Input:</b> root[] = [8, 7, 10, 2, N, 9, 13]<b><br></b><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700425/Web/Other/blobid3_1748007366.webp" alt="" title="" width="184" height="138"/><br><b>Output:</b> true
<b>Explanation: </b>Node 9 is a Dead End in the given BST.</pre>

<b>Constraints:</b><br>1 ≤ number of nodes ≤ 3000<sup><br></sup>1 ≤ node->data ≤ 10<sup>5</sup><sup><br></sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(h)

<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Tree` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Check Whether Bst Contains Dead End Not](https://www.geeksforgeeks.org/check-whether-bst-contains-dead-end-not/)
