<h1 align="center">Reach the Nth point</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 31.23%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 77K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There are<b> N </b>points on the road, you can step ahead by 1 or 2 . If you start from a point 0, and can only move from point <b>i</b> to point <b>i+1</b> after taking a step of length one, find the number of ways you can reach at point <b>N.</b> 

<b>Example 1:</b>

<pre><b>Input: <br></b>N =<b> </b>4
<b>Output: <br></b>5
<b>Explanation:</b> Number of ways to reach at 4th
point are {1, 1, 1, 1}, {1, 1, 2},
{1, 2, 1} {2, 1, 1}, {2, 2}.

</pre>

<b>Example 2:</b>

<pre><b>Input: </b>N = 5
<b>Output: </b>8
<b>Explanation: </b>Number of ways to reach at 5th
point are {1, 1, 1, 1, 1},
{1, 1, 1, 2}, {1, 1, 2, 1}, {1, 2, 1, 1},
{2, 1, 1, 1}{1, 2, 2}, {2, 1, 2}, {2, 2, 1}
</pre>

<b>Your Task:</b><br>You don't need to read or print anyhting. Your task is to complete the function <b>nthPoint()</b> which takes <b>N</b> as input parameter and returns the total number of ways <b>modulo 10<sup>9</sup> + 7 </b>to reach at <b>N<sup>th</sup> </b>point.

<b>Expected Time Complexity: </b>O(N)<br><b>Expected Space Complexity: </b>O(N)

<b>Constraints:</b><br>1 ≤ N ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Morgan Stanley` `Amazon` `Intel`

### Related Articles
- [Count Ways Reach Nth Stair](https://www.geeksforgeeks.org/count-ways-reach-nth-stair/)
