<h1 align="center">Sum 1 to n Divisors</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 43.37%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 218K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a positive integer <b>n,</b> The task is to find the value of <b>Σ<sub>i </sub></b><b>F(i)</b> where <b>i is from 1 to n</b> and function <i><b>F(i)</b></i> is defined as the sum of all divisors of <b>i</b>.

<b>Examples:</b>

<pre><b>Input:</b> n = 4
<b>Output: </b>15
<b>Explanation:</b>
F(1) = 1
F(2) = 1 + 2 = 3
F(3) = 1 + 3 = 4
F(4) = 1 + 2 + 4 = 7<br>So, F(1) + F(2) + F(3) + F(4)
    = 1 + 3 + 4 + 7 = 15<br></pre>

<pre><b>Input:</b> n = 5
<b>Output: </b>21
<b>Explanation:
</b>F(1) = 1
F(2) = 1 + 2 = 3
F(3) = 1 + 3 = 4
F(4) = 1 + 2 + 4 = 7
F(5) = 1 + 5 = 6<br>So,  F(1) + F(2) + F(3) + F(4) + F(5)
    = 1 + 3 + 4 + 7 + 6 = 21</pre>

<pre><b>Input: </b>n = 1
<b>Output: </b>1
<b>Explanation:
</b>F(1) = 1<br>So,  F(1) = 1 </pre>

<b>Constraints:</b><br>1 <= n <= 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Mathematical` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Sum Divisors 1 N](https://www.geeksforgeeks.org/sum-divisors-1-n/)
