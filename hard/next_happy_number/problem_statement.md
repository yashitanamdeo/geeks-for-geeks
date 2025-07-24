<h1 align="center">Next Happy Number</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.97%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 36K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

For a given non-negative integer <b>N</b>, find the next smallest Happy Number. A number is called <b>Happy</b> if it leads to 1 after a <b>sequence of steps</b>. Wherein at each step the number is replaced by the sum of squares of its digits that is, if we start with Happy Number and keep replacing it with sum of squares of its digits, we reach 1 at some point. <br> <br><b>Example 1:</b>

<pre><b>Input:
</b>N = 8<b>
Output:
</b>10<b>
Explanation:</b>
Next happy number after 8 is 10 since
1*1 + 0*0 = 1
</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N = 10<b>
Output
</b>13<b>
Explanation:
</b>After 10, 13 is the smallest happy number because
1*1 + 3*3 = 10, so we replace 13 by 10 and 1*1 + 0*0 = 1.</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>nextHappy()</b> which takes an integer <b>N</b> as input parameters and returns an integer, next Happy number after N.

<b>Expected Time Complexity:</b> O(Nlog<sub>10</sub>N)<br><b>Expected Space Complexity:</b> O(1)<br> <br><b>Constraints:</b><br>1<=N<=10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Recursion` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Happy Number](https://www.geeksforgeeks.org/happy-number/)
