<h1 align="center">Leftmost and rightmost nodes of binary tree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 52.58%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 56K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a Binary Tree of size N, Print the corner nodes ie- the node at the leftmost and rightmost of each level.

<b>Note: </b>Don't print a new line after printing all the corner nodes.

<b>Example 1:</b>

<pre><b>Input :</b>
         1
       /  \
     2      3
    / \    / \
   4   5  6   7    
<b>Output:</b> 1 2 3 4 7
<b>Explanation:</b>
Corners at level 0: 1
Corners at level 1: 2 3
Corners at level 2: 4 7
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>

        10
      /    \
     20     30
    / \  
   40  60
<b>Output: </b>10 20 30 40 60</pre>

<b>Your Task:  </b><br>You dont need to read input. Complete the function <b>printCorner() </b>which takes root node as input parameter and prints the corner nodes separated by spaces. The left corner should be printed before the right for each level starting from level 0.<br><b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(number of nodes in a level)

<b>Constraints:</b><br>1 ≤ N ≤ 10^5


<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Print Leftmost And Rightmost Nodes Of A Binary Tree](https://www.geeksforgeeks.org/print-leftmost-and-rightmost-nodes-of-a-binary-tree/)
