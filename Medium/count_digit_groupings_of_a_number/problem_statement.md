<h1 align="center">Count digit groupings of a number</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 59.38%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 34K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>str</b> consisting of digits, you can divide it into <b>sub-groups</b> by separating the string into substrings. For example, "112" can be divided as {"1", "1", "2"}, {"11", "2"}, {"1", "12"}, and {"112"}.

A v<b>alid grouping</b> can be done if you are able to divide <b>sub-groups</b> where the <b>sum of digits</b> in a <b>sub-group </b>is <b>less than or equal to</b> the <b>sum of the digits </b>of the <b>sub-group </b>immediately right to it. Your task is to determine the <b>total number </b>of <b>valid groupings</b> that could be done for a given string.

<b>Example 1: </b>

<pre><b>Input: <br></b>str = "1119"
<b>Output: <br></b>7
<b>Explanation: <br></b>One valid grouping is {"1", "11", "9"}.<br>Sum of digits of first sub-group ("1") is 1,<br>for the second sub-group ("11"), it is 2,<br>and for the third one ("9"), it is 9.<br>As the sum of digits of the sub-groups is <br>in increasing order, it forms a valid grouping.<br>Other valid grouping are {"1", "119"}, {"1","1","19"}, 
{"1","1","1","9"}, {"11","19"}, {"111","9"} and {"1119"}
are six other valid groupings.
</pre>

<b>Example 2:</b>

<pre><b>Input: <br></b>str = "12"
<b>Output: <br></b>2
<b>Explanation: <br></b>{"1","2"} and {"12"} are two valid groupings.
</pre>

<b>Your Task:</b><br>You don't need to read or print anything. Your task is to complete the function <b>TotalCount()</b> which takes the string <b>str </b>as input parameter and returns total possible groupings.<br>

<b>Expected Time Complexity: O(N<sup>3</sup>)</b> where N is the length of the string.<br><b>Expected Space Complexity: O(N<sup>2</sup>)</b>

<b>Constraints:</b><br>1 <= N <= 100<br>str<sub>i </sub>∈ {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Count Groupings Number Sum Digits Every Sub Group Less Equals Immediate Right Sub Group](https://www.geeksforgeeks.org/count-groupings-number-sum-digits-every-sub-group-less-equals-immediate-right-sub-group/)
