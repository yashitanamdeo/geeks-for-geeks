<h1 align="center">Print N-bit binary numbers having more 1s than 0s</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 56.08%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 48K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a positive integer <b>n</b>. Your task is to generate a string list<b> </b>of all<b> n-bit binary numbers</b> where, for any prefix of the number, there are <b>more or an equal</b> number of 1's than 0's. The numbers should be sorted in <b>decreasing order of magnitude</b>.

<b>Example 1:</b>

<pre><b>Input:</b>  <br>n = 2
<b>Output:</b> <br>{"11", "10"}
<b>Explanation:</b> Valid numbers are those where each prefix has more 1s than 0s:<br>11: all its prefixes (1 and 11) have more 1s than 0s.
10: all its prefixes (1 and 10) have more 1s than 0s.<br>So, the output is "11, 10".
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>  <br>n = 3
<b>Output:</b> <br>{"111", "110", "101"}
<b>Explanation:</b> Valid numbers are those where each prefix has more 1s than 0s.<br>111: all its prefixes (1, 11, and 111) have more 1s than 0s.
110: all its prefixes (1, 11, and 110) have more 1s than 0s.<br>101: all its prefixes (1, 10, and 101) have more 1s than 0s.<br>So, the output is "111, 110, 101".</pre>

<b>User Task:</b><br>Your task is to complete the function <b>NBitBinary() </b>which takes a single integer <b>n</b> as input and returns the <b>list of strings in decreasing order</b>. You need not take any input or print anything.

<b>Expected Time Complexity: </b>O(|2<sup>n</sup>|)<br><b>Expected Auxiliary Space: </b>O(2<sup>n</sup>)

<b>Constraints:</b><br>1 <= n <= 15


<hr>

### Tags
- **Topic Tags:** `Strings` `Recursion` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Print N Bit Binary Numbers 1s 0s Prefixes](https://www.geeksforgeeks.org/print-n-bit-binary-numbers-1s-0s-prefixes/)
