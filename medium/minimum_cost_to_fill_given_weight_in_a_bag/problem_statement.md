<h1 align="center">Minimum cost to fill given weight in a bag</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 25.56%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 72K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>cost[]</b> of positive integers of size <b>n</b> and an integer <b>w</b>, where cost[i] represents the cost of an i kg packet of oranges, the task is to find the minimum cost to buy exactly w kg of oranges. The cost array has a 1-based indexing. If buying exactly w kg of oranges is impossible, then return -1.<br><b>Note:</b><br>1. <b>cost[i] = -1</b> means that <b>i</b> kg packet of orange is unavailable.<br>2.  It may be assumed that there is an infinite supply of all available packet types.

<b>Example 1:</b>

<pre><b>Input</b>: <br>n = 5<br>cost[] = {20, 10, 4, 50, 100} <br>w = 5
<b>Output:</b> <br>14
<b>Explanation</b>: <br>Purchase the 2kg packet for 10 coins and the 3kg packet for 4 coins to buy 5kg of oranges for 14 coins.</pre>

<b>Example 2:</b>

<pre><b>Input</b>: <br>n = 5<br>cost[] = {-1, -1, 4, 3, -1}<br>w = 5
<b>Output:</b> <br>-1
<b>Explanation</b>: <br>It is not possible to buy 5 kgs of oranges.</pre>

<b>Your Task:  </b><br>You don't need to read input or print anything. Complete the function <b>minimumCost() </b>which takes integers <b>n</b> and <b>w, </b>and integer array <b>cost[] </b>as input parameters and returns the minimum cost to buy exactly w kg of oranges, If buying exactly w kg of oranges is impossible, then return -1.

<b>Expected Time Complexity:</b> O(<b>n*w</b>)<br><b>Expected Auxiliary Space:</b> O(<b>n*w</b>)

<b>Constraints:</b><br>1 ≤ n, w ≤ 2*10<sup>2</sup><br>1 ≤ cost[i] ≤ 10<sup>5</sup><br>cost[i] ≠ 0


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Minimum Cost To Fill Given Weight In A Bag](https://www.geeksforgeeks.org/minimum-cost-to-fill-given-weight-in-a-bag/)
