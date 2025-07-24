<h1 align="center">Walls Coloring II</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.15%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 25K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There is a row of <b>N</b> walls in Geeksland. The king of Geeksland ordered Alexa to color all the walls on the occasion of New Year. Alexa can color each wall with one of the <b>K</b> colors. The cost associated with coloring each wall with a particular color is represented by a 2D <b>costs</b> array of size <b>N * K</b>. For example, costs[0][0] is the cost of coloring wall 0 with color 0; costs[1][2] is the cost of coloring wall 1 with color 2, and so on... Find the minimum cost to color all the walls such that no two adjacent walls have the same color.

<b>Note: </b><b>If you are not able to paint all the walls, then you should return -1.</b>

<b>Example 1:</b>

<pre><b>Input:</b>
N = 4, K = 3
costs[][] = {{1, 5, 7},
             {5, 8, 4},
             {3, 2, 9},
             {1, 2, 4}}

<b>Output:</b>
8
<b>Explanation:</b>
Paint wall 0 with color 0. Cost = 1
Paint wall 1 with color 2. Cost = 4
Paint wall 2 with color 1. Cost = 2
Paint wall 3 with color 0. Cost = 1
Total Cost = 1 + 4 + 2 + 1 = 8</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N = 5, K = 1
costs[][] = {{5},
             {4},
             {9},
             {2},
             {1}}
<b>Output:</b>
-1
<b>Explanation:</b>
It is not possible to color all the walls under the given conditions.</pre>

<br><br><b>Your Task:</b>

Your task is to complete the function <b>minCost() </b>which takes a 2D integer matrix <b>costs </b>as the only argument and returns an integer, representing the minimum cost to paint all the walls. If you are not able to paint all the walls, then you should return -1<br><br><b>Expected Time Complexity: O(N*K)<br>Expected Space Complexity: O(N*K)</b>

<b>Constraints:</b>

- 0 <= N <= 10<sup>3</sup>
- 0 <= K <= 10<sup>3</sup>
- 1 <= costs[i][j] <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming`
- **Company Tags:** `None`

### Related Articles
- [Min Cost To Color All Walls Such That No Adjacent Walls Have Same Color](https://www.geeksforgeeks.org/min-cost-to-color-all-walls-such-that-no-adjacent-walls-have-same-color/)
