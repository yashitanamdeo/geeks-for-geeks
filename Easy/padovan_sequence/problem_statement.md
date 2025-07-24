<h1 align="center">Padovan Sequence</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 34.96%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 64K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a number <b>n</b>, find the <b>n<sup>th</sup></b> number in the <i>Padovan Sequence</i>.


A <i>Padovan Sequence</i> is a sequence which is represented by the following recurrence relation<br>P(n) = P(n-2) + P(n-3)<br>P(0) = P(1) = P(2) = 1


<i>Note</i>: Since the output may be too large, compute the answer modulo <b>10^9+7</b>.

<b>Examples :</b>

<pre><b>Input: </b>n = 3
<b>Output:</b> 2
<b>Explanation</b>: We already know, P<sub>1</sub> + P<sub>0</sub> = P<sub>3 </sub>and P<sub>1 </sub>= 1 and P<sub>0</sub> = 1
</pre>

<pre><b>Input</b>: n = 4
<b>Output:</b> 2
<b>Explanation</b>: We already know, P<sub>4  </sub>= P<sub>2</sub> + P<sub>1 </sub>and P<sub>2</sub> = 1 and P<sub>1</sub> = 1<br></pre>

<b>Expected Time Complexity: </b>O(n)<br><b>Expected Auxiliary Space: </b>O(1)

<b>Constraints:</b><br>1 <= n <= 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `series` `Modular Arithmetic` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Padovan Sequence](https://www.geeksforgeeks.org/padovan-sequence/)
