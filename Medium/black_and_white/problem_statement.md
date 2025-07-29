<h1 align="center">Black and White</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.2%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 27K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given the chessboard dimensions. Find out the number of ways we can place a black and a white Knight on this chessboard such that they cannot attack each other.

<b>Note:</b><br>
The knights have to be placed on different squares. A knight can move two squares horizontally and one square vertically (L shaped), or two squares vertically and one square horizontally (L shaped). The knights attack each other if one can reach the other in one move.

<b>Example 1:</b>

<pre><b>Input:
</b>N = 2, M = 2
<b>Output: </b>12 
<b>Explanation</b>: There are 12 ways we can place a black and a white Knight on this chessboard such that they cannot attack each other.

</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N = 2, M = 3
<b>Output: </b>26
<b>Explanation</b>: There are 26 ways we can place a black and a white Knight on this chessboard such that they cannot attack each other.
</pre>

<b>Your Task:</b><br>
Your task is to complete the function <b>numOfWays() </b>which takes the chessboard dimensions N and M as inputs and returns the number of ways we can place 2 Knights on this chessboard such that they cannot attack each other. Since this number can be very large, return it modulo 10<sup>9</sup>+7.

<b>Expected Time Complexity: </b>O(N*M).<br>
<b>Expected Auxiliary Space: </b>O(1).

<b>Constraints:</b><br>
1 <= N * M <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Backtracking` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Count Ways To Place Knights Moving In L Shape In Chessboard](https://www.geeksforgeeks.org/count-ways-to-place-knights-moving-in-l-shape-in-chessboard/)
