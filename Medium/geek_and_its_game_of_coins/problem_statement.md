<h1 align="center">Geek and its Game of Coins</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 42.49%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 44K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given three numbers <b>n</b>, <b>x</b>, and <b>y</b>, Geek and his friend are playing a coin game. In the beginning, there are <b>n</b> coins. In each move, a player can pick <b>x</b>, <b>y</b>, or <b>1</b> coin. Geek always starts the game. The player who picks the last coin wins the game. The task is to determine whether Geek will win the game or not if both players play optimally.

<b>Example 1:</b>

<pre><b>Input</b>: <br>n = 5<br>x = 3<br>y = 4
<b>Output:</b> <br>1
<b>Explanation</b>:<br>There are 5 coins, every player can pick 1 or 3 or 4 coins on his/her turn. Geek can win by picking 3 coins in first chance. Now 2 coins will be left so his friend will pick one coin and now Geek can win by picking the last coin.</pre>

<b>Example 2:</b>
<pre><b>Input</b>:<br>n = 2<br>x = 3<br>y = 4
<b>Output:<br></b>0
<b>Explanation</b>: <br>Geek picks 1 coin and then his friend picks 1 coin.</pre>

<b>Your Task: </b><br>You don't need to read input or print anything. Complete the function <b>findWinner() </b>which takes <b>n</b><b>, x, </b>and<b> y </b>as input parameters and returns 1 if Geek can win otherwise 0.<br><br><b>Expected Time Complexity:</b> O(n)<br><b>Expected Auxiliary Space:</b> O(n)
 
<b>Constraints:</b><br>1 ≤ <b>n, x, y</b> ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Coin Game Winner Every Player Three Choices](https://www.geeksforgeeks.org/coin-game-winner-every-player-three-choices/)
