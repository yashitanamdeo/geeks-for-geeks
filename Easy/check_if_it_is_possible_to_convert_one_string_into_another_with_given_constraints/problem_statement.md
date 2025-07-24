<h1 align="center">Check if it is possible to convert one string into another with given constraints</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.91%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 21K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings S and T, which contains three characters i.e <b>'A', 'B'</b> and <b>'#' </b>only. Check whether it is possible to convert the first string into another string by performing following operations on string first.<br>
1- A can move towards Left only<br>
2- B can move towards Right only<br>
3- Neither A nor B should cross each other<br>
<b>Note:</b> Moving i'th character towards Left one step means swap i'th with (i-1)'th charecter [ i-1>=0 ]. Moving i'th character towards Right one step means swap i'th with (i+1)'th charecter [ i+1< string's length ]. 

<b>Example 1:</b>

<pre><b>Input:</b>
S=#A#B#B#   
T=A###B#B
<b>Output:</b>
1
<b>Explanation:</b>
A in S is right to the A in T 
so A of S can move easily towards
the left because there is no B on
its left positions and for first B 
in S is left to the B in T so B 
of T can move easily towards the 
right because there is no A on its
right positions and it is same for 
next B so S can be easily converted
into T.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
S=#A#B# 
T=#B#A#
<b>Output:</b>
0
<b>Explanation:</b>
Here first A in S is left to the 
A in T and according to the condition,
A cant move towards right,so S cant 
be converted into T.</pre>

<br>
<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>isItPossible() </b>which takes the two strings S, T and their respective lengths M and N as input parameters and returns 1 if S can be converted into T. Otherwise, it returns 0.

<br>
<b>Expected Time Complexity: </b>O(M+N) where M is size of string S and N is size of string T.<br>
<b>Expected Auxillary Space: </b>O(1)<br>
 

<b>Constraints:</b><br>
1<=M,N<=100000


<hr>

### Tags
- **Topic Tags:** `Strings` `constructive algo` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Check If It Is Possible To Convert One String Into Another](https://www.geeksforgeeks.org/check-if-it-is-possible-to-convert-one-string-into-another/)
