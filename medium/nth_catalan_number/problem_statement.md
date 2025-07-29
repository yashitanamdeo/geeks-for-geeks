<h1 align="center">Nth Catalan Number</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 31.06%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 137K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a number <b>n</b>. The task is to find the <b>n<sup>th</sup> catalan number</b>.<br>The first few Catalan numbers for <b>n = 0, 1, 2, 3, </b>… are <b>1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …<br></b><b>Catalan Number </b>for <b>n</b> is equal to the number of expressions containing <b>n</b> pairs of parenthesis that are correctly matched, i.e., for each of the n(' there exist n ')' on there right and vice versa.<br><b>Note:</b> Positions start from 0 as shown above.

<b>Examples:</b>

<pre><b>Input: </b>n = 3
<b>Output: </b>5<b><br>Explanation: </b>Possible expressions are, ((())), (()()), ()(()), (())(), ()()()<b><br></b></pre>

<pre><b>Input: </b>n = 4
<b>Output: </b>14<br><b>Explantions: </b>There are total 14 valid combinations which can be formed using 4 parenthesis.</pre>

<b>Constraints:</b><br>1 <= n <= 19

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Mathematical` `Algorithms`
- **Company Tags:** `Amazon`

### Related Articles
- [Program Nth Catalan Number](https://www.geeksforgeeks.org/program-nth-catalan-number/)
