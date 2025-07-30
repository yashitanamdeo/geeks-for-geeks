<h1 align="center">Walls Coloring</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 61.74%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 19K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There is a row of <b>N</b> walls in Geeksland. The king of Geeksland ordered Alexa to color all the walls on the occasion of New Year. Alexa can color each wall with either pink, black, or yellow. The cost associated with coloring each wall with a particular color is represented by a 2D array <b>colors</b> of size <b>N*3</b> , where <b>colors[i][0]</b>, <b>colors[i][1]</b>, and <b>colors[i][2]</b> is the cost of painting ith wall with colors pink, black, and yellow respectively.

You need to find the minimum cost to color all the walls such that no two adjacent walls have the same color.

<b>Example 1:</b>

<pre><b>Input:</b>
N = 3
colors[][] = {{14, 2, 11},
             {11, 14, 5},
             {14, 3, 10}}
<b>Output:</b>
10
<b>Explanation:</b>
Color wall 0 with black. Cost = 2. 
Color wall 1 with yellow. Cost = 5. 
Color wall 2 with black. Cost = 3.
Total Cost = 2 + 5 + 3 = 10</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N = 2
colors[][] = {{1, 2, 3},
             {1, 4, 6}}
<b>Output:</b>
3
<b>Explanation:</b>
Color wall 0 with black. Cost = 2
Color wall 1 with pink. Cost = 1
Total Cost = 1 + 2 = 3</pre>

<b>Your Task:</b>

Your task is to complete the function <b>minCost()</b> which takes the 2D integer array <b>colors</b> and an integer <b>N</b> as the input parameters and returns an integer, representing the minimum cost to color all the walls.

<b>Expected Time Complexity: </b>O(N).<br>
<b>Expected Auxiliary Space: </b>O(N).

<b>Constraints:</b>

- 1 <= N <= 10<sup>5</sup>
- 1 <= colors[i][0], colors[i][1], colors[i][2] <= 10<sup>4</sup>


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming`
- **Company Tags:** `None`

### Related Articles
- [Min Cost To Color All Walls Such That No Adjacent Walls Have Same Color](https://www.geeksforgeeks.org/min-cost-to-color-all-walls-such-that-no-adjacent-walls-have-same-color/)
