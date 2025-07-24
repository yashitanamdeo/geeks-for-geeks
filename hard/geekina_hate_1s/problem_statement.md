<h1 align="center">Geekina Hate 1s</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 57.82%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 26K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

It is a universal fact that Geekina hates 1s however it is also known that Geekina loves the integers having atmost <b>k</b> 1s (set-bits) in their binary representation. 

Geekina demanded <b>n<sup>th</sup></b> such non-negative number from Geek, and being a good friend of Geek, now it's your responsibility to tell him that number.

<b>Note:</b> The test cases are generated such that the answer always exists and will fit in the 64-bit data type.

<b>Example 1:</b>

<pre><b>Input:</b><br>n = 5<br>k = 1<br><b>Output:</b><br>8<br><b>Explanation:</b><br>Following numbers are loved by Geekina -<br>0 = (0)<sub>2</sub><br>1 = (1)<sub>2</sub><br>2 = (10)<sub>2</sub><br>4 = (100)<sub>2</sub><br>8 = (1000)<sub>2</sub></pre>

<b>Example 2:</b>

<pre><b>Input:</b><br>n = 6<br>k = 2<br><b>Output:</b><br>5<br><b>Explanation:</b><br>Following numbers are loved by Geekina -<br>0 = (0)<sub>2</sub><br>1 = (1)<sub>2</sub><br>2 = (10)<sub>2</sub><br>3 = (11)<sub>2</sub><br>4 = (100)<sub>2</sub><br>5 = (101)<sub>2</sub></pre>

<b>Your Task:<br></b>This is a function problem. The input is already taken care of by the driver code. You only need to complete the function findNthNumer() that takes n and k as input parameters. Return the n<sup>th</sup> number having at most k set-bits.

<b>Expected Time Complexity:</b> O(k*log(n) + constant)<br><b>Expected Auxiliary Space:</b> O(k*log(n) + constant)

<b>Constraints:<br></b>1 <= n <= 10<sup>9<br></sup>1 <= k <= 63


<hr>

### Tags
- **Topic Tags:** `Binary Search` `Bit Magic`
- **Company Tags:** `None`
