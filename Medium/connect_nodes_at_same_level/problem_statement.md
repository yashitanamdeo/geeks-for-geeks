<h1 align="center">Connect Nodes at Same Level</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 71.19%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 20K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree, connect the nodes that are at the same level. The structure of the tree Node contains an addition nextRight pointer for this purpose.

Initially, all the nextRight pointers point to garbage values. Your should set these pointers to point next right for each node.<br><br>       10                       10 ------> NULL<br>      / \                       /      \<br>     3   5       =>     3 ------> 5 --------> NULL<br>    / \     \               /  \           \<br>   4   1   2          4 --> 1 -----> 2 -------> NULL

<b>Note: </b>The generated output will contain 2 lines. First line contains the level order traversal of the tree and second line contains the inorder traversal of the tree.

<b>Examples:</b>

<pre><b>Input: </b>root = [3, 1, 2]
     3
   /  \
  1    2
<b>Output:
</b>[3, 1, 2]
[1, 3, 2]<b>
Explanation: </b>The connected tree is
       3 ------> NULL
     /   \
    1---> 2 -----> NULL
</pre>

<pre><b>Input: </b>root = [10, 20, 30, 40, 60]
      10
    /   \
   20   30
  /  \
 40  60
<b>Output:
</b>[10, 20, 30, 40, 60]
[40, 20, 60, 10, 30]<b>
Explanation: </b>The connected tree is
        10 ---> NULL
       /   \
     20---> 30 ---> NULL
   /   \
 40---> 60 ---> NULL</pre>

<b>Constraints:</b>


1 ≤ number of nodes ≤ 10<sup>5</sup><br>0 ≤ node->data ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Flipkart` `Accolite` `Amazon` `Microsoft` `OYO Rooms` `Ola Cabs` `Oracle` `Adobe` `Google` `Boomerang Commerce` `Xome`

### Related Articles
- [Connect Nodes At Same Level With O1 Extra Space](https://www.geeksforgeeks.org/connect-nodes-at-same-level-with-o1-extra-space/)
- [Connect Nodes At Same Level](https://www.geeksforgeeks.org/connect-nodes-at-same-level/)
- [Connect Nodes Level Level Order Traversal](https://www.geeksforgeeks.org/connect-nodes-level-level-order-traversal/)

### Related Interview Experiences
- [Amazon Interview Experience Set 355 1 Year Experienced](https://www.geeksforgeeks.org/amazon-interview-experience-set-355-1-year-experienced/)
- [Microsoft Interview Experience Set 98 On Campus For Idc](https://www.geeksforgeeks.org/microsoft-interview-experience-set-98-on-campus-for-idc/)
