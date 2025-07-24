<h1 align="center">Binary Modulo</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.34%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 34K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a binary <b>string s</b> and an <b>integer m</b>. You need to return an <b>integer r</b>. Where <b>r = k%m</b>, k is the binary equivalent of <b>string s</b>.

<b>Example 1:</b>

<pre><b>Input:</b>
s = "101" 
m = 2
<b>Output:</b>
1
<b>Explanation:</b> Here k=5 because (101)<sub>2</sub> = (5)<sub>10</sub>.
Hence 5 mod 2 = 1.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
s = "1000"
m = 4
<b>Output:</b>
0
<b>Explanation:</b> Here k=8 and m=4 hence 
r = k mod m = 8 mod 4 = 0.</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function modulo() which takes the string s and integer m as input parameters and returns the value of r as described above.

<b>Expected Time Complexity:</b> O(N)<br><b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>1 <= len(s) <= 10<sup>7</sup><br>1 <= m <= 100


<hr>

### Tags
- **Topic Tags:** `Mathematical` `Bit Magic`
- **Company Tags:** `None`

### Related Articles
- [Modulo Of A Large Binary String](https://www.geeksforgeeks.org/modulo-of-a-large-binary-string/)
