<h1 align="center">Maximum Winning score</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 72.44%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 7K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

In an online game, <b>N</b> blocks are arranged in a hierarchical manner. All the blocks are connected together by a total of N-1 connections. Each block is given an ID from 1 to N. A block may be further connected to other blocks. Each block is also assigned a specific<b> point value</b>.

A player starts from Block 1. She must move forward from each block to a directly connected block until she reaches the final block, which has no further connection. When the player lands on a block, she <b>collects the point value</b> of that block. The players score is calculated as the <b>product of point values</b> that the player collects.<br>
Find the maximum score a player can achieve.<br>
<b>Note: </b>The answer can always be represented with 64 bits.

<br>
<b>Example 1:</b>

<pre><b>Input:
</b>     4
    / \
   2   8
  / \ / \
 2  1 3  4
<b>Output: </b>128<b>
Explanation: </b>Path in the given tree 
goes like 4, 8, 4 which gives the max
score of 4x8x4 = 128.
</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>     10
   /    \
  7      5
          \
           1
<b>Output: </b>70<b>
Explanation: </b>The path 10, 7 gives a 
score of 70 which is the maximum possible.
</pre>

<br>
<b>Your Task:</b><br>
You don't need to take input or print anything. Your task is to <b>complete </b>the function <b>findMaxScore() </b>that takes <b>root </b>as input and returns max score possible.

<br>
<b>Expected Time Complexity: </b>O(N).<br>
<b>Expected Auxiliary Space: </b>O(Height of the Tree).

<br>
<b>Constraints:</b><br>
1 ≤ Number of nodes ≤ 10<sup>3</sup><br>
1 ≤ Data on node ≤ 10 
It is guaranteed that the answer will always fit in the 64-bit Integer


<hr>

### Tags
- **Topic Tags:** `Binary Search Tree` `Data Structures`
- **Company Tags:** `Morgan Stanley`

### Related Interview Experiences
- [Morgan Stanley Interview Experience For Summer Internship 2021](https://www.geeksforgeeks.org/morgan-stanley-interview-experience-for-summer-internship-2021/)
