<h1 align="center">Minimum Steps Required</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 59.74%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 25K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>str</b> consisting of only two characters <b>'a'</b> and <b>'b'</b>. You need to find the minimum steps required to make the string empty by removing consecutive <b>a's</b> and <b>b's</b>.

<b>Example 1:</b>

<pre><b>Input:</b>
str = "bbaaabb"
<b>Output:</b>
2
<b>Explanation:</b>
Operation 1: Removal of all <b>a's</b> modifies str to "bbbb".
Operation 2: Removal of all remaining <b>b's</b> makes str
empty.
Therefore, the minimum number of operations required
is 2.</pre>

<b>Example 2:</b>

<pre><b>Input:</b>
str = "aababaa"
<b>Output:</b>
3
<b>Explanation:</b>
Operation 1: Removal of b's modifies str to "aaabaa".
Operation 2: Removal of b's modifies str = "aaaaa".
Operation 3: Removal of all remaining a's makes str 
empty.
Therefore, the minimum number of operations required 
is 3.
</pre>

<b>Your Task:</b>

You need to complete the function <b>minSteps() </b>which takes a string <b>str </b>as the only input parameter and returns an integer, denoting the minimum steps required to make the string empty.

<b>Expected Time Complexity: </b>O(N), where N = length of string <b>str<br>
Expected Space Complexity: </b>O(1)

<b>Constraints:</b>

- 1 <= str.length() <= 10<sup>5</sup>
- 'a' <= str[i] <= 'b'


<hr>

### Tags
- **Topic Tags:** `Greedy`
- **Company Tags:** `None`

### Related Articles
- [Minimum Steps To Empty String Of As And Bs](https://www.geeksforgeeks.org/minimum-steps-to-empty-string-of-as-and-bs/)
