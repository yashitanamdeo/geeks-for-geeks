<h1 align="center">Print Pattern</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 56.39%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 98K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a number <b>n</b>, print a <b>sequence of numbers</b> starting from <b>n</b>. Each next number in the sequence is <b>n - 5</b>, and this continues recursively until the number becomes <b>less than</b> or <b>equal to 0</b>. After that, print the sequence in reverse order, <b>adding 5</b> each time, until it reaches back to the original number <b>n</b>.<br><b>Note:</b> You must not use loops.

<b>Examples:</b>

<pre><b>Input:</b> n = -16
<b>Output:</b> [-16]
<b>Explanation:</b> Since -16 is less than zero so it will remain same.</pre>

<pre><b>Input:</b> n = 10
<b>Output: [</b>10, 5, 0, 5, 10]
<b>Explanation:</b> The value decreases until it is greater or equal to 0. After that it increases and stops when it becomes 10 again.</pre>

<b>Constraints:</b><br>-10<sup>5</sup> ≤ n ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `pattern-printing` `Recursion` `Algorithms`
- **Company Tags:** `Microsoft`
