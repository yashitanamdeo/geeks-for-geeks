<h1 align="center">Maximum Value</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 65.51%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 18K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree, find the largest value in each level.

<br>
<b>Example 1:</b>

<pre><b>Input:</b>
        1
       / \
      2   3 
<b>Output:</b>
1 3
<b>Explanation:</b>
At 0 level, values of nodes are {1}
                 Maximum value is 1
At 1 level, values of nodes are {2,3}
                Maximum value is 3
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
        4
       / \
      9   2
     / \   \
    3   5   7 
<b>Output:</b>
4 9 7
<b>Explanation:</b>
At 0 level, values of nodes are {4}
                 Maximum value is 4
At 1 level, values of nodes are {9,2}
                 Maximum value is 9
At 2 level, values of nodes are {3,5,7}
                 Maximum value is 7</pre>

 

<b>Your Task:</b>

You don't need to read input or print anything.Your task is to complete the function <b>maximumValue</b>() that takes root node as input parameter and returns a list of integers containing the maximum value at each level. The size of the resultant list should be equal to the height of the binary tree and result[i] should store the maximum value at level i.

<br>
<b>Expected Time Complexity: </b>O(N), where N is the number of nodes.<br>
<b>Expected Auxiliary Space: </b>O(H), where H is the height of binary tree.

<br>
<b>Constraints:</b><br>
1 ≤ Number of nodes ≤ 10^4<br>
1 ≤ Data of a node ≤ 10^5


<hr>

### Tags
- **Topic Tags:** `DFS` `Tree` `implementation` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon`

### Related Articles
- [Largest Value Level Binary Tree](https://www.geeksforgeeks.org/largest-value-level-binary-tree/)

### Related Interview Experiences
- [Amazon Interview Experience For Fte 6 Months Sde 1 Internship Amazewow](https://www.geeksforgeeks.org/amazon-interview-experience-for-fte-6-months-sde-1-internship-amazewow/?ref=rp)
