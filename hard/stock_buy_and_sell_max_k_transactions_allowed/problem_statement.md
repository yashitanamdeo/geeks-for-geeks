<h1 align="center">Stock Buy and Sell – Max K Transactions Allowed</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 48.35%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 57K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

In the stock market, a person buys a stock and sells it on some future date. You are given an array <b>prices[]</b> representing stock prices on different days and a positive integer <b>k</b>, find out the <b>maximum</b> profit a person can make in at-most <b>k </b>transactions. 

A transaction consists of buying and subsequently selling a stock and new transaction can start only when the <b>previous transaction</b> has been<b> completed.</b>

<b>Examples :</b>

<pre><b>Input: </b>prices[] = [10, 22, 5, 80], k = 2
<b>Output:</b> 87
<b>Explaination:<br></b>1st transaction: Buy at 10 and sell at 22. 
2nd transaction : Buy at 5 and sell at 80.<br>Total Profit will be 12 + 75 = 87.</pre>

<pre><b>Input:</b> prices[] = [20, 580, 420, 900], k = 3<br><b>Output:</b> 1040
<b>Explaination:</b> <br>1st transaction: Buy at 20 and sell at 580. <br>2nd transaction : Buy at 420 and sell at 900.<br>Total Profit will be 560 + 480 = 1040.</pre>

<pre><b>Input: </b>prices[] = [100, 90, 80, 50, 25],  k = 1<b><br></b><b>Output:</b> 0
<b>Explaination:</b> Selling price is decreasing continuously
leading to loss. So seller cannot have any profit.</pre>

<b>Constraints:</b><br>1 ≤ prices.size() ≤ 10<sup>3<br></sup>1 ≤ k ≤ 200<br>1 ≤ prices[i] ≤ 10<sup>3</sup>

## Expected Complexities
- Time Complexity: O(n * k)
- Auxiliary Space: O(k)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Accolite` `Amazon` `Microsoft`

### Related Articles
- [Maximum Profit By Buying And Selling A Share At Most K Times](https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-k-times/)

### Related Interview Experiences
- [Amazon Interview Experience For 6 Months Internship](https://www.geeksforgeeks.org/amazon-interview-experience-for-6-months-internship/)
