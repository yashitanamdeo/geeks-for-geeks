<h1 align="center">Maximum sum of Non-adjacent nodes</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 55.35%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 91K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 45m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>binary tree</b> with a value associated with each node. Your task is to select a <b>subset of nodes</b> such that the sum of their values is <b>maximized</b>, with the condition that no two selected nodes are <b>directly connected</b> that is, if a node is included in the subset, neither its <b>parent</b> nor its <b>children</b> can be included.

<b>Examples:</b>

<pre><b>Input:</b> root[] = [11, 1, 2]<b><br></b>
<b>Output: </b>11<b>
Explanation: </b>The maximum sum is obtained by selecting the node 11.<br></pre>

<pre><b>Input:</b> root[] = [1, 2, 3, 4, N, 5, 6]
<br><b>Output: </b>16<b>
Explanation: </b>The maximum sum is obtained by selecting the nodes 1, 4, 5, and 6, which are not directly connected to each other. Their total sum is 16.  <br><br></pre>

<b>Constraints:</b><br>1 ≤ no. of nodes in the tree ≤ 10<sup>4</sup>
1 ≤ Node.val ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Flipkart` `Amazon` `Google`

### Related Articles
- [Maximum Sum Nodes Binary Tree No Two Adjacent](https://www.geeksforgeeks.org/maximum-sum-nodes-binary-tree-no-two-adjacent/)

### Related Interview Experiences
- [Flipkart Interview Experience For Sde 1 On Campus 2019 2](https://www.geeksforgeeks.org/flipkart-interview-experience-for-sde-1-on-campus-2019-2/)
