<h1 align="center">Search Pattern (Z-algorithm)</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.7%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 12K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings, one is a text string and the other is a pattern string. The task is to print the indexes of all the occurrences of the pattern string in the text string. For printing, Starting Index of a string should be taken as 1.

<b>Example 1:</b>

<pre><b>Input:</b>
S = "batmanandrobinarebat", pat = "bat"
<b>Output:</b> 1 18
<b>Explanation</b>: The string "bat" occurs twice
in S, one starts are index 1 and the other
at index 18. 
</pre>

<b>Example 2:</b>

<pre><b>Input</b>: 
S = "abesdu", pat = "edu"
<b>Output:</b> -1
<b>Explanation</b>: There's not substring "edu"
present in S.
</pre>

<br>
<b>Your Task:</b><br>
You don't need to read input or print anything. Your task is to complete the function <b>search() </b>which takes the string S and the string pat as inputs and returns an array denoting the start indices (<b>1-based</b>) of substring pat in the string S. 

<b>Note: </b>You don't need to return -1 yourself when there are no possible answers, just return an empty list.<br>
<br>
<b>Expected Time Complexity: </b>O(|S|).<br>
<b>Expected Auxiliary Space: </b>O(|S|).

<br>
<b>Constraints:</b><br>
1 ≤ |S| ≤ 10<sup>5</sup><br>
1 ≤ |pat| ≤ |S|


<hr>

### Tags
- **Topic Tags:** `Strings` `Pattern Searching` `Data Structures` `Algorithms`
- **Company Tags:** `Microsoft`

### Related Articles
- [Z Algorithm Linear Time Pattern Searching Algorithm](https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/)
