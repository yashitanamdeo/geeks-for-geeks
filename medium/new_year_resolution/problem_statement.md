<h1 align="center">New Year Resolution</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 52.56%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 34K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

As the clock struck midnight on New Year's Eve, Geek bid farewell to the wasted moments of 2023, realizing the untapped potential of GFG's Problem of the Day. 


<b>His 2024 resolution: Solve POTD every day.</b>


Eager to earn coins for GFG Merchandise, Geek faces new rules:

1. <b>Earning Coin:</b> Geek can accumulate coins[i] by solving the POTD on the ith day, where 1 <= coins[i] <= 2024 and the sum of coins <= 2024.
1. <b>Merchandise Eligibility:</b> To purchase merchandise, Geeks should solve <b>atleast one POTD</b> and the coins earned must be divisible by 20 or 24, or precisely equal to 2024.
Geek's resolutions often fades over time. Realistically, he can only commit to active participation for N (where N ≤ 366) days. Given the value of N and number of coins associated with each POTD, can Geek strategically solve some (or all) POTDs to become eligible for redeeming merchandise?

<b>Example 1:</b>

<pre><b>Input:</b><br>N = 8<br>coins = [5, 8, 9, 10, 14, 2, 3, 5]<br><br><b>Output: </b>1<br><br><b>Explanation:</b><br>Geek can fulfill the criteria in many ways.<br>One such way is to solve POTD on 4th and 5th day.<br>Another way is to solve POTD on 1st, 4th and 8th day.</pre>

<b>Example 2:</b>

<pre><b>Input:<br></b>N = 5<br>coins = [1, 2, 3, 4, 5]<br><br><b>Output: </b>0<br><br><b>Explanation: </b>There is no way Geek can become eligible.</pre>

<b>Your Task: <br></b>You don't need to read input or print anything. Complete the function isPossible() which takes n and coins[ ] as input parameters and returns a boolean value.

<b>Expected Time Complexity:</b> O(N*(Sum of coins))<br><b>Expected Auxiliary Space: </b>O(N*(Sum of coins))

<b>Constraints:<br></b>1 <= N <= 366<br>1 <= coins[i] <= 2024<br>1 <= Sum of coins <=  2024


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Recursion`
- **Company Tags:** `None`
