<h1 align="center">Copy Set Bits in Range</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 39.22%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 56K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two numbers <b>X</b> and <b>Y</b>, and a range [<b>L</b>, <b>R</b>] where 1 <= L <= R <= 32. You have to copy the set bits of <b>'Y'</b> in the range L to R in<b> 'X'.</b> Return this modified X.

Note: Range count will be from Right to Left & start from 1.

<b>Example 1:</b>

<pre><b>Input:</b> 
X = 44, Y = 3 
L = 1,  R = 5
<b>Output:</b> <br>47
<b>Explaination:</b> <br>Binary represenation of 44 and 3 is 101100 and 0000<b>11</b>. So in the range 1 to 5 there are two set bits of 3 (1st & 2nd position). If those are set in 44 it will become 1011<b>11</b> which is 47.</pre>

<b>Example 2:</b>

<pre><b>Input:</b> 
X = 16, Y = 2
L = 1,  R = 3
<b>Output:</b> 18
<b>Explaination:</b> Binary represenation of 16 and 2 is 10000 and <b>10</b>. If the mentioned conditions are applied then 16 will become 100<b>10</b> which is 18.</pre>

<b>Your Task:</b><br>You do not need to read input or print anything. Your task is to complete the function <b>setSetBit()</b> which takes the numbers X, Y, L and R as input parameters and returns the modified value of X.

<b>Expected Time Complexity:</b> O(R - L)<br><b>Expected Auxiliary Space:</b> O(1)

<b>Constraints:</b><br>1 ≤ X, Y ≤ 10<sup>9</sup><br>1 ≤ L ≤ R ≤ 32


<hr>

### Tags
- **Topic Tags:** `Bit Magic` `Data Structures`
- **Company Tags:** `D-E-Shaw` `Adobe`

### Related Articles
- [Copy Set Bits In A Range](https://www.geeksforgeeks.org/copy-set-bits-in-a-range/)
