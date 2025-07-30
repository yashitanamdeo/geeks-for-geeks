<h1 align="center">Odd Even Problem</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.0%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 43K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>s</b> of <b>lowercase English </b>characters, determine whether the summation of <b>x</b> and <b>y</b> is<b> <i>EVEN</i> </b>or<b> <i>ODD.</i></b><br>where:

1. <b><i>x</i></b> is the count of distinct characters that occupy <b>even </b>positions in the English alphabet and have <b>even </b>frequency. 
1.  <b><i>y</i></b> is the count of distinct characters that occupy <b>odd </b>positions in the English alphabet and have <b>odd </b>frequency.
<b>Ex:</b> string = "ab" here 'a' has an odd(1) position in the English alphabet & has an odd(1) frequency in the string so a is odd but b has an even(2) position in the English alphabet & has odd(1) frequency so it doesn't count(since string doesn't have 2 b's) so the final answer x + y = 1+0 = 1(odd) would be "ODD".

<b>Note</b>: 

- Return "<b>EVEN</b>" if the sum of x & y is even otherwise return "<b>ODD</b>".
- You need to find index of characters in the english alphabet <b>"abcdefghijklmnopqrstuvwxyz".</b>
<b>Examples :</b>

<pre><b>Input: </b>s = "abbbcc"
<b>Output:</b> ODD
<b>Explanation: </b>x = 0 and y = 1 so (x + y) is ODD. 'a' occupies 1st place(odd) in english alphabets and its frequency is odd(1), 'b' occupies 2nd place(even) but its frequency is odd(3) so it doesn't get counted and 'c' occupies 3rd place(odd) but its frequency is even(2) so it also doesn't get counted.
</pre>

<pre><b>Input: </b>s = "nobitaa"
<b>Output:</b> EVEN
<b>Explanation:</b> Here n, b, t & a would not count since doesn't match with the <b>even</b> condition but o & i will be counted as it satisfies the <b>odd</b> conditions so x = 0 and y = 2 so (x + y) is EVEN.
</pre>

 

<b>Expected Time Complexity: </b>O(|s|)<br><b>Expected Auxiliary Space: </b>O(1) 

<b>Constraints:</b><br>1 ≤ |s| ≤ 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Hash` `Strings` `Bit Magic` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Check Whether Given Number Even Odd](https://www.geeksforgeeks.org/check-whether-given-number-even-odd/)
