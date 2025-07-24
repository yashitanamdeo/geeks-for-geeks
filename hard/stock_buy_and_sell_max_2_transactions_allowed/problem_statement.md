<h1 align="center">Stock Buy and Sell – Max 2 Transactions Allowed</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.13%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 70K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

In daily share trading, a trader buys shares and sells them on the same day. If the trader is allowed to make <b>at most</b> <b>2 </b>transactions in a day, find out the <b>maximum</b> profit that a share trader could have made. 

You are given an array <b>prices[]</b> representing stock prices throughout the day. Note that the second transaction can only start after the first one is complete (buy->sell->buy->sell).

<b>Examples:</b>

<pre><b>Input: </b>prices[] = [10, 22, 5, 75, 65, 80]
<b>Output: </b>87
<b>Explanation: <br></b>Trader will buy at 10 and sells at 22. <br>Profit earned in 1st transaction = 22 - 10 = 12. <br>Then he buys at 5 and sell at 80. <br>Profit earned in 2nd transaction = 80 - 5 = 75. <br>Total profit earned = 12 + 75 = 87. </pre>

<pre><b>Input: </b>prices[] = [2, 30, 15, 10, 8, 25, 80]
<b>Output: </b>100
<b>Explanation: <br></b>Trader will buy at 2 and sells at 30. <br>Profit earned in 1st transaction = 30 - 2 = 28. <br>Then he buys at 8 and sell at 80. <br>Profit earned in 2nd transaction = 80 - 8 = 72. <br>Total profit earned = 28 + 72 = 100.</pre>

<b>Constraints:<br></b>1 <= prices.size() <= 10<sup>5<br></sup>1 <= prices[i] <= 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Dynamic Programming` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon` `Facebook`

### Related Articles
- [Maximum Profit By Buying And Selling A Share At Most Twice](https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/)
