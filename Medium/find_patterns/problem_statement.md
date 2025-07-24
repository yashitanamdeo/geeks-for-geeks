<h1 align="center">Find patterns</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.24%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 26K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings S and W. Find the number of times W appears as a subsequence of string S where every character of string S can be included in forming at most one subsequence.<br>
 

<b>Example 1: </b> 

<pre><b>Input:</b> 
 S = "abcdrtbwerrcokokokd" 
 W = "bcd" 
<b>Output:</b> 
 2
<b>Explanation:</b> 
The two subsequences of string W are
{ S<sub>1</sub> , S<sub>2</sub> , S<sub>3</sub> } and { S<sub>6</sub><sub> </sub>, S<sub>11</sub> , S<sub>18</sub> }
(Assuming 0- based indexing).
</pre>

 

<b>Example 2: </b>

<pre><b>Input:</b> 
S = "ascfret" 
W = "qwer" 
<b>Output:</b> 
0
<b>Explanation:</b>
No valid subsequences are possible.
</pre>

 

<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>numberOfSubsequences()</b> which takes the string S and string W<b> </b>as input parameters and returns the number of subsequences of string W in string S.

 

<b>Expected Time Complexity:</b> O(N<sup>2</sup>)<br>
<b>Expected Auxiliary Space:</b> O(N)<br>
 

<b>Constraints:</b><br>
1<=|S|<=1000<br>
1<=|W|<=|S|


<hr>

### Tags
- **Topic Tags:** `Strings` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Find Number Times String Occurs Given String](https://www.geeksforgeeks.org/find-number-times-string-occurs-given-string/)
