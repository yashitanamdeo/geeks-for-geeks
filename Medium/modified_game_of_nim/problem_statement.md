<h1 align="center">Modified Game of Nim</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 57.13%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 32K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array <b>A</b> of <b>n </b>elements. There are two players player 1 and player 2.<br>A player can choose any of element from an array and remove it. If the bitwise XOR of all remaining elements equals 0 after removal of the selected element, then that player loses. Find out the winner if player 1 starts the game and they both play their best. 

<b>Note:</b> If the xor of the array is initially 0, then player 1 is considered as winner.

<b>Example 1:</b>

<pre><b>Input:</b> <br>n = 3
A = [3, 3, 2]
<b>Output:</b> <br>2
<b>Explaination:</b> <br>Optimal removal of values are 3, 2, 3 sequentially. Then the array is empty. So player 2 wins.</pre>

<b>Example 2:</b>

<pre><b>Input:</b> <br>n = 2
A = [3, 3]
<b>Output:</b> <br>1
<b>Explaination:</b> <br>Since the xor of an array is already 0, player 1 wins.</pre>

<b>Your Task:</b><br>You do not need to read input or print anything. Your task is to complete the function <b>findWinner()</b> which takes the number <b>n</b> and the array <b>A</b> as input parameters and returns an integer denoting the winner.

<b>Expected Time Complexity: </b>O(n)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>1 ≤ n ≤ 10<sup>5</sup><br>0 ≤ A[i] ≤ 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Bit Magic` `Game Theory` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Find Winner Nim Game](https://www.geeksforgeeks.org/find-winner-nim-game/)
