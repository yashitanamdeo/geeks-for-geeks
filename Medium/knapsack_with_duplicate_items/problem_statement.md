<h1 align="center">Knapsack with Duplicate Items</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 52.13%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 199K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a set of items, each with a weight and a value, represented by the array <b>wt</b> and <b>val</b> respectively. Also, a knapsack with a weight limit <b>capacity</b>.<br>The task is to fill the knapsack in such a way that we can get the maximum profit. Return the maximum profit.<br><b>Note:</b> Each item can be taken any number of times.

<b>Examples:</b>

<pre><b>Input:</b> val = [1, 1], wt = [2, 1], capacity = 3
<b>Output:</b> 3
<b>Explanation: </b>The optimal choice is to pick the 2nd element 3 times.
</pre>

<pre><b>Input: </b>val[] = [6, 1, 7, 7], wt[] = [1, 3, 4, 5], capacity = 8
<b>Output:</b> 48
<b>Explanation: </b>The optimal choice is to pick the 1st element 8 times.<br></pre>

<pre><b>Input: </b>val[] = [6, 8, 7, 100], wt[] = [2, 3, 4, 5], capacity = 1
<b>Output:</b> 0
<b>Explanation: </b>We can't pick any element .hence, total profit is 0.</pre>

<b>Constraints:</b><br>1 <= val.size() = wt.size() <= 1000<br>1 <= capacity <= 1000<br>1 <= val[i], wt[i] <= 100

## Expected Complexities
- Time Complexity: O(n*capacity)
- Auxiliary Space: O(capacity)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Amazon` `Google`

### Related Articles
- [Unbounded Knapsack Repetition Items Allowed](https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/)

### Related Interview Experiences
- [Amazon Interview Experience Set 389 Campus Full Time](https://www.geeksforgeeks.org/amazon-interview-experience-set-389-campus-full-time/)
