<h1 align="center">Divisor Game</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 70.69%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 31K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Alice and Bob take turns playing a game, with Alice starting first.<br>Initially, there is a number <b>n</b> on the chalkboard. On each player's turn, that player makes a move consisting of:

- Choosing any <b>x</b> with <b>0 < x < n</b>  and <b>n % x == 0</b>.
- Replacing the number <b>n</b> on the chalkboard with <b>n - x</b>.
Also, if a player cannot make a move, they lose the game.<br>Return <b>true</b> if and only if Alice wins the game, assuming both players play <b>optimally.</b>

 

<b>Example 1:</b>

<pre><b>Input:</b><br>n = 2<br><b>Output: </b>True<br><b>Explanation:</b> Alice chooses 1, and Bob has no more moves.</pre>

 

<b>Example 2:</b>

<pre><b>Input:</b><br>n = 3<br><b>Output: </b>False<br><b>Explanation:</b> Alice chooses 1, Bob chooses 1, and Alice has no more moves.</pre>

 

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>divisorGame()</b> which takes an integer <b>n </b>as a parameter and returns true if Alice wins the game.

<b>Expected Time Complexity:</b> O(1)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>1 ≤ n ≤ 10<sup>3</sup>


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Recursion` `Backtracking` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Optimal Strategy For The Divisor Game Using Dynamic Programming](https://www.geeksforgeeks.org/optimal-strategy-for-the-divisor-game-using-dynamic-programming/)
