<h1 align="center">Largest subtree sum in a tree</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.83%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 27K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary tree. The task is to find subtree with maximum sum in the tree and return its sum.

<b>Example 1:</b>

<pre><b>Input:</b>
              1
            /   \
           2      3
          / \    / \
         4   5  6   7
<b>Output: </b>28
<b>Explanation:</b> 
As all the tree elements are positive,
the largest subtree sum is equal to
sum of all tree elements.</pre>

<pre>
<b>Example 2:</b>
<b>Input:</b>
               1
            /    \
          -2      3
          / \    /  \
         4   5  -6   2
<b>Output: </b>7
<b>Explanation: </b>
Subtree with largest sum is : 
  -2
 /  \ 
4    5
Also, entire tree sum is also 7.</pre>

 

<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>findLargestSubtreeSum</b><b>()</b> which takes the root of a binary tree and returns an integer.<br>
 

<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>
1 <= N <= 10^5<br>
-10^3 <= tree.val <= 10^3


<hr>

### Tags
- **Topic Tags:** `Tree`
- **Company Tags:** `None`

### Related Articles
- [Find Largest Subtree Sum Tree](https://www.geeksforgeeks.org/find-largest-subtree-sum-tree/)
