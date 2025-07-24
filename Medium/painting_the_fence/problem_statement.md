<h1 align="center">Painting the Fence</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 32.89%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 121K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 40m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a fence with <b>n </b>posts and <b>k</b> colours, find out the number of ways of painting the fence so that <b>not more than two </b>consecutive posts have the same colours.<br>Answers are guaranteed to be fit into a 32 bit integer.

<b>Examples:</b>

<pre><b>Input: </b>n = 3, k = 2 
<b>Output:</b> 6
<b>Explanation</b>: Let the 2 colours be 'R' and 'B'. We have following possible combinations:<br>1. RRB
2. RBR
3. RBB
4. BRR
5. BRB
6. BBR</pre>

<pre><b>Input: </b>n = 2, k = 4 
<b>Output:</b> 16
<b>Explanation</b>: After coloring first post with 4 possible combinations, you can still color next posts with all 4 colors. Total possible combinations will be 4x4=16</pre>

<b>Constraints:</b><br>1 ≤ n ≤ 300<br>1 ≤ k ≤ 10<sup>5</sup><br>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Dynamic Programming` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Painting Fence Algorithm](https://www.geeksforgeeks.org/painting-fence-algorithm/)
