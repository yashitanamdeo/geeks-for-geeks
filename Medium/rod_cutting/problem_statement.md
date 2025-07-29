<h1 align="center">Rod Cutting</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 60.66%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 180K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a rod of length <b>n </b>inches and an array <b>price[]</b>, where <b>price[i]</b> denotes the value of a piece of length <b>i</b>. Your task is to determine the <b>maximum</b> value obtainable by <b>cutting up </b>the rod and selling the <b>pieces</b>.

<b>Note:</b> n = size of price, and price[] is <b>1-indexed </b>array.

<b>Example:</b>

<pre><b>Input:</b> price[] = [1, 5, 8, 9, 10, 17, 17, 20]<br><b>Output:</b> 22<br><b>Explanation:</b> The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6, i.e., 5 + 17 = 22.</pre>

<pre><b>Input: </b>price[] = [3, 5, 8, 9, 10, 17, 17, 20]<br><b>Output: </b>24<br><b>Explanation: </b>The maximum obtainable value is 24 by cutting the rod into 8 pieces of length 1, i.e, 8*price[1] = 8*3 = 24.<br></pre>

<pre><b>Input: </b>price[] = [3]<br><b>Output: </b>3<br><b>Explanation:</b> There is only 1 way to pick a piece of length 1.</pre>

<b>Constraints:</b><br>1 ≤ price.size() ≤ 10<sup>3</sup><br>1 ≤ price[i] ≤ 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Dynamic Programming` `Data Structures` `Algorithms`
- **Company Tags:** `Google`

### Related Articles
- [Cutting A Rod Dp 13](https://www.geeksforgeeks.org/cutting-a-rod-dp-13/)
