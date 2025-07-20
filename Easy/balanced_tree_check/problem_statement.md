<h1 align="center">Balanced Tree Check</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 43.15%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 339K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>binary tree</b>, determine if it is <b>height-balanced</b>. A binary tree is considered height-balanced if the absolute difference in heights of the left and right subtrees is at most 1 for every node in the tree.

<b>Examples:</b>

<pre><b>Input: </b>root[] = [10, 20, 30, 40, 60]<br><br>   
<b>Output:</b> true
<b>Explanation:</b> The height difference between the left and right subtrees at all nodes is at most 1. Hence, the tree is balanced.</pre>

<pre><b>Input: </b>root[] = [1, 2, 3, 4, N, N, N, 5]
   
<b>Output:</b> false
<b>Explanation:</b> The height difference between the left and right subtrees at node 2 is 2, which exceeds 1. Hence, the tree is not balanced.</pre>

<pre><b>Input: </b>root[] = [1, 2, N, N, 3]
   
<b>Output: </b>false
<b>Explanation:</b> The height difference between the left and right subtrees at node 1 is 2, which exceeds 1. Hence, the tree is not balanced.</pre>

<b>Constraints:</b><br>0 <= number of nodes <= 5000<br>- 10<sup>4</sup> <= node->data <= 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(h)

<hr>

### Tags
- **Topic Tags:** `Tree` `Data Structures`
- **Company Tags:** `Amazon` `Microsoft` `Walmart`

### Related Articles
- [How To Determine If A Binary Tree Is Balanced](https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/)

### Related Interview Experiences
- [Walmart Lab Interview Experience Set 8 Off Campus 3 Years Experience](https://www.geeksforgeeks.org/walmart-lab-interview-experience-set-8-off-campus-3-years-experience/)
