<h1 align="center">Sum-string</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.56%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 44K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>s</b> consisting of digits, determine whether it can be classified as a <b>sum-string</b>.

A <b>sum-string</b> is a string that can be split into <b>more</b> <b>than two </b>non-empty substrings such that:

 

-  
The <b>rightmost substring</b> is equal to the <b>sum of the two substrings immediately before it</b> (interpreted as integers).

 
-  
This condition must apply <b>recursively</b> to the substrings before it.

 
-  
The <b>rightmost substring</b> (and any number in the sum) <b>must not contain leading zeroes</b>, unless the number is exactly '0'.


<b>Examples:</b>

<pre><b>Input: </b>s = "12243660"
<b>Output: </b>true
<b>Explanation: </b>The string can be split as {"12", "24", "36", "60"} where each number is the sum of the two before it:
36 = 12 + 24, and 60 = 24 + 36. Hence, it is a sum-string.</pre>

<pre><b>Input:</b> s <b>= "</b>1111112223"
<b>Output: </b>true
<b>Explanation: </b>Split the string as {"1", "111", "112", "223"}, where:
112 = 1 + 111 and 223 = 111 + 112. Hence, it follows the sum-string rule.<br></pre>

<pre><b>Input</b>: s = "123456"<br><b>Output</b>: false<br><b>Explanation</b>: There is no valid split of the string such that each part satisfies the sum-string property recursively.</pre>

<b>Constraints:<br></b>1 ≤ s.size() ≤ 100<br>String consists of characters from '0' to '9'.

## Expected Complexities
- Time Complexity: O(n^3)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Strings` `Recursion` `Backtracking` `Data Structures` `Algorithms`
- **Company Tags:** `Nutanix`

### Related Articles
- [Check Given String Sum String](https://www.geeksforgeeks.org/check-given-string-sum-string/)
