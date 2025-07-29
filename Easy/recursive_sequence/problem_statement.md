<h1 align="center">Recursive sequence</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.57%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 53K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 7m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

A function <b>F</b> is defined as follows <b>F(n)= (1) +(2*3) + (4*5*6) ... upto n terms </b>(look at the examples for better clarity). Given an integer <b>n,</b> determine the <b>F(n)</b>.

<b>Note: </b>As the answer can be very large, return the answer modulo <b>10<sup>9</sup>+7</b>.

<b>Example 1:</b>

<pre><b>Input:</b> n = 5
<b>Output:</b> 365527
<b>Explanation:</b> <br>F(5) = 1 + 2*3 + 4*5*6 + 7*8*9*10 + 11*12*13*14*15 = 365527.</pre>

<b>Example 2:</b>

<pre><b>Input:</b> n = 7
<b>Output:</b> 6997165<br>
<b>Explanation:</b> <br>F(7) = 1 + 2*3 + 4*5*6 + 7*8*9*10 + 11*12*13*14*15 + <br>16*17*18*19*20*21 + 22*23*24*25*26*27*28 = 6006997207.<br>6006997207 % 10<sup>9</sup>+7 = 6997165<br></pre>

<b>Your Task:</b><br>You do not need to read input or print anything. Your task is to complete the function <b>sequence()</b> which takes an integer <b>n </b>as an input parameter and returns the value of <b>F(n).</b>

<b>Expected Time Complexity:</b> O(n<sup>2</sup>)<br><b>Expected Space Complexity:</b> O(1)

<b>Constraints:</b><br>1 ≤ n ≤ 10<sup>3</sup>


<hr>

### Tags
- **Topic Tags:** `Mathematical` `Recursion` `Algorithms`
- **Company Tags:** `MAQ Software`

### Related Articles
- [Solving Fn 1 23 456 N Using Recursion](https://www.geeksforgeeks.org/solving-fn-1-23-456-n-using-recursion/)
