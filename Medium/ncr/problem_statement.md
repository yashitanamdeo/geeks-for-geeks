<h1 align="center">nCr</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 14.82%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 344K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two integer values <b>n </b>and <b>r</b>, the task is to find the value of Binomial Coefficient<b> </b><b><sup>n</sup>C<sub>r</sub></b>

- A [binomial coefficient](https://www.geeksforgeeks.org/coefficient-in-binomial-expansion/) <b><b><sup>n</sup></b></b><b>C</b><b><b><sub>r</sub></b> </b>can be defined as the coefficient of<b> x<sup>r</sup> </b>in the expansion of <b>(1 + x)<sup>n</sup> </b>that gives the number of ways to choose r objects from a set of n objects without considering the order.
- The binomial coefficient <b><b><b><sup>n</sup></b></b>C<b><b><sub>r </sub></b></b></b>is calculated as : C(n,r) = n! / r! * (n-r) !
<b>Note:</b> If r is greater than n, return <b>0</b>.<br>It is guaranteed that the value of <sup>n</sup><b>C</b><sub>r</sub> will fit within a 32-bit integer.

<b>Examples:</b>

<pre><b>Input:</b> n = 5, r = 2
<b>Output:</b> 10
<b>Explaination:</b> The value of <sup>5</sup>C<sub>2</sub> is calculated as 5!/(5−2)!*2! = 5!/3!*2! = 10.</pre>

<pre><b>Input:</b> n = 2, r = 4
<b>Output:</b> 0
<b>Explaination:</b> Since r is greater than n, thus <b><b><b><sup>2</sup></b></b></b>C<b><b><b><sub>4</sub> </b></b></b>= 0</pre>

<pre><b>Input:</b> n = 5, r = 0<br><b>Output:</b> 1
<b>Explaination:</b> The value of <sup>5</sup>C<sub>0</sub> is calculated as 5!/(5−0)!*0! = 5!/5!*0! = 1.</pre>

<b>Constraints:</b><br>1 ≤ n ≤ 100<br>0 ≤ r ≤ 100

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Mathematical` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Program Calculate Value Ncr](https://www.geeksforgeeks.org/program-calculate-value-ncr/)
