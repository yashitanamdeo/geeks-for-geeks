<h1 align="center">Find the String</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 72.98%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 26K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two integers<b> N</b> and <b>K, </b>the task is to find the string <b>S</b> of <b>minimum </b>length such that it contains <b>all possible strings </b>of size <b>N</b> as a <b>substring</b>. The characters of the string should be from integers ranging from <b>0 to K-1</b>.  

<b>Example 1:</b>

<pre><b>Input:</b>
N = 2, K = 2
<b>Output:</b> 
00110
<b>Explanation: 
</b>Allowed characters are from 0 to k-1 (i.e., 0 and 1).<br>There are 4 string possible of size N=2 
(i.e "00", "01","10","11")
"00110" contains all possible string as a 
substring. It also has the minimum length.</pre>

<b>Example 2:</b>

<pre><b>Input:
</b>N = 2, K = 3
<b>Output: 
</b>0010211220
<b>Explanation: <br></b>Allowed characters are from 0 to k-1 (i.e., 0, 1 and 2).<b><br></b>There are total 9 strings possible
of size N, given output string has the minimum
length that contains all those strings as substring.
</pre>

<b>Your Task: </b><br>You don't need to read input or print anything. Complete the function<b> findString( )</b> which takes the integer <b>N</b> and the integer <b>K</b> as input parameters and returns the string.<br><b>Note:</b> In case of multiple answers, return <b>any string of minimum length </b>which satisfies above condition. The driver will print the <b>length</b> of the string. In case of wrong answer it will print <b>-1</b>.

<b>Expected Time Complexity:</b> O(K<sup>N</sup>K)<br><b>Expected Space Complexity: </b>O(K<sup>N</sup>N)

<b>Constraints:</b><br>1 ≤ N ≤ 4<br>1 <u><</u> K <u><</u> 10<br>1 <u><</u> K<sup>N</sup>N < 10<sup>6</sup>


<hr>

### Tags
- **Topic Tags:** `Strings` `Graph` `Backtracking` `Data Structures` `Algorithms`
- **Company Tags:** `Google`

### Related Articles
- [Min Length String With All Substrings Of Size N](https://www.geeksforgeeks.org/min-length-string-with-all-substrings-of-size-n/)
