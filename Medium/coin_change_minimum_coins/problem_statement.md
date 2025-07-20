<h1 align="center">Coin Change (Minimum Coins)</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 26.74%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 261K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array <b>coins[]</b>, where each element represents a coin of a <b>different</b> denomination, and a target value <b>sum</b>. You have an <b>unlimited</b> supply of each coin type {coins1, coins2, ..., coinsm}. 

Your task is to determine the <b>minimum</b> number of coins needed to obtain the target <b>sum</b>. If it is not possible to form the sum using the given coins, return <b>-1</b>.

<b>Examples:</b>

<pre><b>Input:</b> coins[] = [25, 10, 5], sum = 30<br><b>Output:</b> 2<br><b>Explanation:</b> Minimum 2 coins needed, 25 and 5  </pre>

<pre><b>Input:</b> coins[] = [9, 6, 5, 1], sum = 19<br><b>Output: </b>3<br><b>Explanation:</b> 19 = 9 + 9 + 1</pre>

<pre><b>Input:</b> coins[] = [5, 1], sum = 0<br><b>Output: </b>0<br><b>Explanation:</b> For 0 sum, we do not need a coin</pre>

<pre><b>Input:</b> coins[] = [4, 6, 2], sum = 5<br><b>Output: </b>-1<br><b>Explanation:</b> Not possible to make the given sum.</pre>

 
<b>Constraints:</b><br>1 ≤ sum * coins.size() ≤ 10<sup>6</sup>
0 <= sum <= 10<sup>4</sup>
1 <= coins[i] <= 10<sup>4</sup>
1 <= coins.size() <= 10<sup>3</sup>

## Expected Complexities
- Time Complexity: O(coins.size * sum)
- Auxiliary Space: O(sum)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Paytm` `Morgan Stanley` `Accolite` `Amazon` `Microsoft` `Samsung` `Snapdeal` `Oracle` `Visa` `Google` `Synopsys`

### Related Articles
- [Find Minimum Number Of Coins That Make A Change](https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/)

### Related Interview Experiences
- [Accolite Interview Experience Set 6 On Campus](https://www.geeksforgeeks.org/accolite-interview-experience-set-6-on-campus/)
