<h1 align="center">Find the N-th character</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 19.13%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 67K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a binary string <b>s</b>. Perform <b>r</b> iterations on string <b>s</b>, where in each iteration <b>0 </b>becomes<b> 01</b> and <b>1 </b>becomes<b> 10</b>. Find the <b>nth</b> character (considering <b>0 based </b>indexing) of the string after performing these <b>r</b> iterations (see examples for better understanding).

<b>Example 1:</b>

<pre><b>Input</b>:
s = "1100"
r = 2
n = 3
<b>Output</b>:
1
<b>Explanation</b>: 
After 1st iteration <b>s</b> becomes "10100101".<br>After 2nd iteration <b>s</b> becomes "100<b>1</b>100101100110".<br>Now, we can clearly see that the character at 3rd index is 1, and so the output.
</pre>

<b>Example 2:</b>

<pre><b>Input</b>:
s = "1010"
r = 1
n = 2
<b>Output</b>:
0
<b>Explanation </b>: 
After 1st iteration <b>s</b> becomes "10<b>0</b>11001".
Now, we can clearly see that the character at 2nd index is 0, and so the output.</pre>

<b>Your task:</b>
You don't need to read input or print anything. Your task is to complete the function <b>nthCharacter()</b> which takes the string <b>s</b> and integers <b>r</b> and <b>n</b> as input parameters and returns the n-th character of the string after performing r operations on s.
 
<b>Expected Time Complexity:</b> O(r*|s|)
<b>Expected Auxilary Space:</b> O(|s|)
 
<b>Constraints</b>: <br>1 ≤ |s| ≤ 10<sup>3</sup><br>1 ≤ r ≤ 20<br>0 ≤ n < |s|


<hr>

### Tags
- **Topic Tags:** `Strings` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Find Ith Index Character In A Binary String Obtained After N Iterations](https://www.geeksforgeeks.org/find-ith-index-character-in-a-binary-string-obtained-after-n-iterations/)
