<h1 align="center">Find position of set bit</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Basic-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.62%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 74K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 1-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a number <b>n</b> having only one ‘1’ and all other ’0’s in its binary representation, find the position of the only set bit. If there are 0 or more than 1 set bit the answer should be -1. The position of set bit '1' should be counted starting with 1 from the LSB side in the binary representation of the number.

<b>Examples:</b>

<pre><b>Input:</b> n =<b> </b>2
<b>Output: </b>2
<b>Explanation: </b>2 is represented as "10" in Binary. As we see there's only one set bit and it's in position 2.<br></pre>

<pre><b>Input:</b><b> </b>n =<b> </b>5
<b>Output: </b>-1
<b>Explanation: </b>5 is represented as "101" in Binary. As we see there's two set bits and thus the output -1.
</pre>

<b>Constraints:</b><br>0 <= n <= 10<sup>8</sup>

## Expected Complexities
- Time Complexity: O(log n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Bit Magic` `Data Structures`
- **Company Tags:** `Microsoft`

### Related Articles
- [Find Position Of The Only Set Bit](https://www.geeksforgeeks.org/find-position-of-the-only-set-bit/)
