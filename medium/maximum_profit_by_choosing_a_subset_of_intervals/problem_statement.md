<h1 align="center">Maximum Profit By Choosing A Subset Of Intervals</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 55.11%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 16K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a list <b>intervals</b> of <b>n</b> intervals, the <b>ith</b> element <b>[s, e, p]</b> denotes the starting point <b>s</b>, ending point <b>e</b>, and the profit <b>p</b> earned by choosing the <b>ith</b> interval. Find the maximum profit one can achieve by choosing a subset of non-overlapping intervals.

Two intervals <b>[s1, e1, p1]</b> and <b>[s2, e2, p2]</b> are said to be non-overlapping if <b>[e1 <= s2]</b> and <b>[s1 < s2]</b>.

<b>Example 1:</b>

<pre><b>Input:</b>
n = 3
intervals = {
{1, 2, 4},
{1, 5, 7},
{2, 4, 4}
}
<b>Output:</b>
8
<b>Explanation:</b>
One can choose intervals [1, 2, 4] and [2, 4, 4] for a 
profit of 8.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
n = 3
intervals = {
{1, 4, 4},
{2, 3, 7},
{2, 3, 4}
}
<b>Output:</b>
7
<b>Explanation:
</b>One can choose interval [2, 3, 7] for a profit of 7.</pre>

<b>Your Task:</b>

You don't need to print or output anything. Complete the function <b>maximum_profit() </b>which takes an integer <b>n </b>and a 2D integer array <b>intervals </b>and returns an integer, denoting the maximum profit which one can get by choosing the non-overlapping intervals.<br><br>Expected Time Complexity: O(nlogn)<br>Expected Space Complexity: O(n)

<b>Constraints:</b>

- 1 <= n and n <= 10<sup>4</sup>
- 1 <= starting point of <b>ith</b> interval < ending point of <b>ith</b> interval <= 10<sup>5</sup>
- 1 <= profit earned by choosing <b>ith</b> interval <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `None`
- **Company Tags:** `None`

### Related Articles
- [Maximum Profit By Choosing A Subset Of Intervals Using Priority Queue](https://www.geeksforgeeks.org/maximum-profit-by-choosing-a-subset-of-intervals-using-priority-queue/)
