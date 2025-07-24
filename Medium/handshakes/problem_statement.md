<h1 align="center">Handshakes</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 48.96%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 19K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

We have N persons sitting on a round table. Any person can do a handshake with any other person. 

     1<br>
2         3<br>
     4

Handshake with 2-3 and 1-4 will cause cross.

In how many ways these N people can make handshakes so that no two handshakes cross each other. N would be even.  <br>
 

<b>Example 1:</b>

<pre><b>Input:</b>
N = 2
<b>Output:</b>
1
<b>Explanation:</b>
{1,2} handshake is
possible.
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
N = 4
<b>Output:</b>
2
<b>Explanation:</b>
{{1, 2}, {3, 4}} are the
two handshakes possible.
{{1, 3}, {2, 4}} is another
set of handshakes possible.
</pre>

<br>
<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>count()</b> which takes an integer <b>N</b> as input parameters and returns an integer, the total number of handshakes possible so that no two handshakes cross each other.<br>
 

<b>Expected Time Complexity:</b> O(2<sup>N</sup>)<br>
<b>Expected Space Complexity:</b> O(1)<br>
 

<b>Constraints:</b><br>
1 <= N <= 30


<hr>

### Tags
- **Topic Tags:** `Recursion` `Algorithms`
- **Company Tags:** `Amazon`

### Related Articles
- [Non Crossing Lines Connect Points Circle](https://www.geeksforgeeks.org/non-crossing-lines-connect-points-circle/)
