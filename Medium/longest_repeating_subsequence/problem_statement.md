<h1 align="center">Longest Repeating Subsequence</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 48.54%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 139K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given string str, find the length of the longest repeating subsequence such that it can be found twice in the given string. 

The two identified subsequences A and B can use the same ith character from string <b>s</b> if and only if that ith character has different indices in A and B. For example, A = "xax" and B = "xax" then the index of the first "x" must be different in the original string for A and B.

<b>Examples :</b>

<pre><b>Input: </b>s = "axxzxy"
<b>Output:</b> 2
<b>Explanation: </b>The given array with indexes looks like
a x x z x y 
0 1 2 3 4 5
The longest subsequence is "xx". It appears twice as explained below.
<b>subsequence A</b>
x x
0 1  <-- index of subsequence A
------
1 2  <-- index of s
<b>subsequence B</b>
x x
0 1  <-- index of subsequence B
------
2 4  <-- index of s
We are able to use character 'x' (at index 2 in s) in both subsequences as it appears on index 1 in subsequence A and index 0 in subsequence B.</pre>

<pre><b>Input: </b>s = "axxxy"
<b>Output:</b> 2
<b>Explanation: </b>The given array with indexes looks like
a x x x y 
0 1 2 3 4
The longest subsequence is "xx". It appears twice as explained below.
<b>subsequence A</b>
x x
0 1  <-- index of subsequence A
------
1 2  <-- index of s
<b>subsequence B</b>
x x
0 1  <-- index of subsequence B
------
2 3  <-- index of s
We are able to use character 'x' (at index 2 in s) in both subsequencesas it appears on index 1 in subsequence A and index 0 in subsequence B.</pre>

<b>Constraints:</b><br>1 <= s.size() <= 10<sup>3</sup>

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(n^2)

<hr>

### Tags
- **Topic Tags:** `Strings` `Dynamic Programming` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon` `Google`

### Related Articles
- [Longest Repeating Subsequence](https://www.geeksforgeeks.org/longest-repeating-subsequence/)
