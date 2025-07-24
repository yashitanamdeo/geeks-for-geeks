<h1 align="center">Another Coin Change Problem</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 54.5%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 25K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given three integers <b>n</b>, <b>k</b>,<b> target</b>, and an array of coins of size <b>n</b>. Find if it is possible to make a change of <b>target </b>cents by using an infinite supply of each coin but the total number of coins used must be exactly equal to <b>k</b>.

<b>Example 1:</b>

<pre><b>Input:</b>
n = 5, k = 3, target = 11
coins = {1, 10, 5, 8, 6}

<b>Output:</b> 
1

<b>Explanation: </b>
2 coins of 5 and 1 coins of 1 can be used 
to make change of 11 i.e. 11 => 5+5+1.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
n = 3, k = 5, target = 25
coins = {7, 2, 4}

<b>Output:</b>
1

<b>Explanation:</b>
3 coins 7, 2 coins of 2 can be used to
make change of 25 i.e. 25 => 7+7+7+2+2.</pre>

<b>Your Task:</b><br>This is a function problem. You only need to complete the function makeChanges() that 3 integers n, k, target, and an array coins as parameters and return True or False.

<b>Expected Time Complexity: </b>O(n*k*target)<br><b>Expected Space Complexity: </b>O(k*target)

<b>Constraints:</b><br>1 <= n, k, coins[i] <= 100<br>1 <= target <= 1000


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Coin Change Problem With Limited Coins](https://www.geeksforgeeks.org/coin-change-problem-with-limited-coins/)
