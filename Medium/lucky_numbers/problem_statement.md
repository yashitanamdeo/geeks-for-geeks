<h1 align="center">Lucky Numbers</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 30.35%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 126K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

A <b>lucky number</b> is defined using a special elimination process:<br>   <b>1.</b> Start with natural numbers: 1, 2, 3, 4, 5, 6, ...<br>   <b>2.</b> In the 1st step, remove every 2nd number.<br>   <b>3.</b> In the 2nd step, remove every 3rd remaining number.<br>   <b>4.</b> In the 3rd step, remove every 4th remaining number, and so on...<br>This continues indefinitely. Given an integer <b>n</b>, determine if it remains after all steps. <br>Return <b>1</b> if <b>n</b> is a lucky number, otherwise return <b>0</b>.

<b>Examples :</b>

<pre><b>Input: </b>n = 5
<b>Output: </b>0<b>
Explanation: </b>5 is not a lucky number as it gets deleted in the second iteration.
</pre>

<pre><b>Input: </b>n = 19
<b>Output: </b>1<b>
Explanation: </b>19 is a lucky number because it does not get deleted throughout the process.</pre>

<b>Constraints:</b><br>1 ≤  n ≤  10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Mathematical` `Recursion` `Algorithms`
- **Company Tags:** `Microsoft`

### Related Articles
- [Lucky Numbers](https://www.geeksforgeeks.org/lucky-numbers/)
