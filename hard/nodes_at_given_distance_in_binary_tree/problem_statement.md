<h1 align="center">Nodes at given distance in binary tree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 32.36%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 86K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree, a target node in the binary tree, and an integer value k, find all the nodes that are at a distance k from the given target node. No parent pointers are available.<br><b>Note</b>: 

- You have to return the list in sorted order.
- The tree will <b>not </b>contain <b>duplicate </b>values.
<b>Examples:</b>

<pre><b>Input:</b> root = [1, 2, 3, 4, 5], target = 2, k = 2   

<b>Output:</b> [3]
<b>Explanation: </b>Nodes at a distance 2 from the given node 2 is 3.
</pre>

<pre><b>Input: </b>root = [1, 2, 3, 4, 5, 6, 7], target = 3, k = 1<br>
<b>Output:</b> [1, 6, 7]<br><b>Explanation:</b> Nodes at a distance 1 from the given target node 3 are 1, 6 & 7.</pre>

<b>Constraints:</b><br>1 ≤ number of nodes ≤ 10<sup>6</sup><br>1 ≤  node->data ≤ 10<sup>9</sup><br>1 ≤ target ≤ 10<sup>9</sup><br>1 ≤ k ≤ 20

## Expected Complexities
- Time Complexity: O(n log n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Flipkart` `Accolite` `Amazon` `Microsoft` `Samsung` `Hike` `Ola Cabs` `Walmart` `Goldman Sachs`

### Related Articles
- [Print Nodes Distance K Given Node Binary Tree](https://www.geeksforgeeks.org/print-nodes-distance-k-given-node-binary-tree/)

### Related Interview Experiences
- [Hike Interview Experience Set 5](https://www.geeksforgeeks.org/hike-interview-experience-set-5/)
- [Ola Cabs Interview Experience Set 3](https://www.geeksforgeeks.org/ola-cabs-interview-experience-set-3/)
- [Samsung Rnd Bangalore Interview 2018](https://www.geeksforgeeks.org/samsung-rnd-bangalore-interview-2018/)
