<h1 align="center">Product of Primes</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 25.39%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 30K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 25m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two numbers <b>L</b> and <b>R</b> (inclusive) find the<b> product of primes </b>within this range. Print the product modulo <b>10<sup>9</sup>+7</b>. If there are no primes in that range you must print 1.

<b>Examples:</b>

<pre><b>Input:</b> L = 1, R = 10
<b>Output:</b> 210
<b>Explaination:</b> The prime numbers are 2, 3, 5 and 7.</pre>

<pre><b>Input:</b> L = 1, R = 20
<b>Output:</b> 9699690
<b>Explaination:</b> The primes are 2, 3, 5, 7, 11, 13, 17 and 19.</pre>

<b>Constraints:</b><br>1 ≤ L ≤ R ≤ 10<sup>9</sup><br>0 ≤ (R - L) ≤ 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O((R-L)*sqrt(R))
- Auxiliary Space: O(sqrt(R))

<hr>

### Tags
- **Topic Tags:** `Prime Number` `sieve`
- **Company Tags:** `None`

### Related Articles
- [Segmented Sieve](https://www.geeksforgeeks.org/segmented-sieve/)
