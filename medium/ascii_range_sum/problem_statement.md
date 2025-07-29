<h1 align="center">ASCII Range Sum</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 56.69%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 9K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>s </b>consisting of lowercase English letters, for every character whose first and last occurrences are at different positions, calculate the sum of ASCII values of characters <b>strictly between</b> its first and last occurrence.<br>Return all such <b>non-zero sums</b> (order does not matter).

<b>Examples:</b>

<pre><b>Input: </b>s = "abacab"<b><br>Output: </b>[293, 294]<b><br></b><b>Explanation: </b>characters 'a' and 'b' appear more than once:<br>'a' : between positions 1 and 5<b> </b>→ characters are b, a, c and ascii sum is 98 + 97 + 99 = 294.<br>'b' : between positions 2 and 6 → characters are a, c, a and ascii sum is 97 + 99 + 97 = 293.<br></pre>

<pre><b>Input:</b> s = "acdac"<b><br>Output: </b>[197, 199]<b><br>Explanation: </b>characters 'a' and 'c' appear more than once:<br>'a' : between positions 1 and 4<b> </b>→ characters are c, d and ascii sum is 99 + 100 = 199.<br>'c' : between positions 2 and 5 → characters are d, a and ascii sum is 100 + 97 = 197.</pre>

<b>Constraints:<br></b>1 ≤ s.size() ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `prefix-sum` `Data Structures` `Hash`
- **Company Tags:** `None`
