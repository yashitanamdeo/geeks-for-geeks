<h1 align="center">Count the nodes at distance K from leaf</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 34.27%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 75K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 45m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree with <b>n </b>nodes and a non-negative integer <b>k</b>, the task is to count the number of <b>special nodes</b>. <br>A node is considered <b>special</b> if there exists at least one leaf in its subtree such that the distance between the node and leaf is exactly <b>k</b>.<br><b>Note:</b> Any such node should be counted only once. For example, if a node is at a distance <b>k</b> from 2 or more leaf nodes, then it would add only 1 to our count.

<b>Examples:</b>

<pre><b>Input:</b>
        1
      /   \
     2     3
   /  \   /  \
  4   5  6    7
          \ 
           8
k = 2
<b>Output: </b>2<b>
Explanation: </b>There are only two unique nodes that are at a distance of 2 units from the leaf node. (node 3 for leaf with value 8 and node 1 for leaves with values 4, 5 and 7) Note that node 2 isn't considered for leaf with value 8 because it isn't a direct ancestor of node 8.
</pre>

<pre><b>Input:</b><b><br></b>          1
         /
        3
       /
      5
    /  \
   7    8
         \
          9
k = 4
<b>Output: </b>1<b>
Explanation: </b>Only one node is there which is at a distance of 4 units from the leaf node.(node 1 for leaf with value 9) </pre>

<b>Constraints:</b><br>1 <= n <= 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(h)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Flipkart` `Microsoft`

### Related Articles
- [Print Nodes Distance K Leaf Node](https://www.geeksforgeeks.org/print-nodes-distance-k-leaf-node/)

### Related Interview Experiences
- [Microsoft Interview Experience Set 76 On Campus](https://www.geeksforgeeks.org/microsoft-interview-experience-set-76-on-campus/)
