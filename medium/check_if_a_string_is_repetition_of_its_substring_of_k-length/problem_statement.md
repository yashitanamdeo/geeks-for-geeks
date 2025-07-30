<h1 align="center">Check if a string is repetition of its substring of k-length</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.15%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 39K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>s</b>, check if it is possible to convert it into a string that is the <b>repetition </b>of a substring of <b>length k</b>. Conversion has to be done by following the steps mentioned below <b>only once</b>:

1. Select two indices <b>i </b>and <b>j </b>(<b>zero-based indexing, i </b>could be equal to <b>j</b>), such that <b>i</b> and <b>j </b>are divisible by <b>k</b>.
1. Select substrings of length <b>k</b> starting from indices <b>i</b> and <b>j.</b>
1. Replace substring starting at index <b>i</b> with substring starting at index <b>j </b>within the string
<b>Note: </b><b>You have to convert the string using the operation only once</b>.

<b>Example 1:</b>

<pre><b>Input:</b>
N = 4<br>K = 2<br>S = "bdac"
<b>Output:</b> 1
<b>Explanation</b>: We can replace either
"bd" with "ac" or "ac" with "bd"
</pre>

<b>Example 2:</b>

<pre><b>Input</b>: 
N = 5<br>K = 2<br>S = "abcde"
<b>Output:</b> 0
<b>Explanation</b>: Since <b>n</b> % <b>k</b> != 0, it's not 
possible to convert <b>s</b> into a string which
is a concatanation of a substring with 
length <b>k</b>.
</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function <b>kSubstrConcat() </b>which takes a string <b>s</b>, its length <b>n </b>and an integer <b>k </b>as inputs and return <b>1</b> if convertion of the given string is possible, else <b>0</b>.

<b>Expected Time Complexity: </b>O(n).<br><b>Expected Auxiliary Space: </b>O(n).

<b>Constraints:</b><br>2 <= k < n <= 10<sup>5</sup>


<hr>

### Tags
- **Topic Tags:** `Strings` `Map` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Convert String Repetition Substring K Length](https://www.geeksforgeeks.org/convert-string-repetition-substring-k-length/)
