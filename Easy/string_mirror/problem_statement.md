<h1 align="center">String Mirror</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.38%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 30K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a string <b>str</b> of length <b>n</b>. You want to choose a non-zero integer k (k<=n), such that you can perform the following operation:<br>Take the prefix of the string of length k and append the reverse of it to itself.<br>Your task is to find the <b>lexicographically smallest</b> string you can get.

<b>Example 1:</b>

<pre><b>Input:</b>
str = "bvdfndkn"
<b>Output:</b>
bb
<b>Explanation:
</b>If we choose k=1, prefix of length k will be "b", reverse of
this prefix will be "b" itself, when we append both we get "bb",
"bb" is the lexicographically smallest string you can get.
If you choose k>1, the resulting string will not be 
lexicographically smaller than "bb".
</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
str = "casd"
<b>Output:</b>
caac
<b>Explanation:
</b>If we choose k=2, prefix of length k will be "ca", reverse of
this prefix will be "ac", when we append both we get "caac",
"caac" is the lexicographically smallest string you can get.
</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>stringMirror()</b> which takes a String <b>str</b> as input, and returns the lexicographically smallest string.

<b>Expected Time Complexity: </b>O(|str|)<br><b>Expected Space Complexity:</b> O(|str|)

<b>Constraints:</b><br>1 <= |str| <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Strings` `Mathematical` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find Lexicographically Smallest String With Prefix Reversal](https://www.geeksforgeeks.org/find-lexicographically-smallest-string-with-prefix-reversal/)
