<h1 align="center">Remove BST keys outside given range</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 59.43%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 17K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given the <b>root </b>of a Binary Search Tree (BST) and two integers <b>l</b> and <b>r</b>, remove all the nodes whose values lie outside the range [l, r].

<b>Note:</b> The modified tree should also be BST and the sequence of the remaining nodes should not be changed.

<b>Examples:</b>

<pre><b>Input: </b>root = [6, -13, 14, N, -8, 13, 15, N, N, 7], l = -10, r = 13
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/913250/Web/Other/blobid0_1760417976.jpg" alt="" title="" width="265" height="246"/>
<b>Output: </b>[6, -8, 13, N, N, 7]<br><b>Explanation: </b>All the nodes outside the range [-10, 13] are removed and the modified tree is a valid BST.
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/913250/Web/Other/blobid1_1760417983.jpg" alt="" title="" width="237" height="224"/>
</pre>

<pre><b>Input: </b>root = [14, 4, 16, 2, 8, 15, N, -8, 3, 7, 10], l = 2, r = 6<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/913250/Web/Other/blobid2_1760444733.jpg" alt="" title="" width="299" height="255"/> <br><b>Output: </b>[4, 2, N, N, 3]
<b>Explanation: </b>All the nodes outside the range [2, 6] are removed and the modified tree is a valid BST.<br><br>   <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/913250/Web/Other/blobid1_1760444076.jpg" alt="" title="" width="187" height="250"/></pre>

<b>Constraints:</b>
1 ≤ number of nodes ≤ 10<sup>4</sup><br>1 ≤ node->data ≤ 10<sup>4</sup>
1 ≤ l ≤ r ≤ 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Data Structures`
- **Company Tags:** `Microsoft` `Samsung`

### Related Articles
- [Remove Bst Keys Outside The Given Range](https://www.geeksforgeeks.org/remove-bst-keys-outside-the-given-range/)

### Related Interview Experiences
- [Samsung Interview Experience For Rd Intern Sri Bangalore](https://www.geeksforgeeks.org/samsung-interview-experience-for-rd-intern-sri-bangalore/)
