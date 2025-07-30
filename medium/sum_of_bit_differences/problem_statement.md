<h1 align="center">Sum of bit differences</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 60.03%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 54K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array integers <b>arr[]</b>, containing <b>n</b> elements, find the sum of <b>bit differences</b> between all pairs of element in the array. <b>Bit difference </b>of a pair <b>(x, y) </b>is the count of different bits at the <b>same positions</b> in binary representations of <b>x</b> and <b>y</b>.<br><b>Note</b>: (x, y) and (y, x) are considered two separate pairs.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [1, 2]
<b>Output:</b> 4
<b>Explanation</b>: All possible pairs of an array are (1, 1), (1, 2), (2, 1), (2, 2). Sum of bit differences = 0 + 2 + 2 + 0 = 4</pre>

<pre><b>Input: </b>arr[] = [1, 3, 5]
<b>Output:</b> 8
<b>Explanation</b>: All possible pairs of an array are (1, 1), (1, 3), (1, 5), (3, 1), (3, 3) (3, 5),(5, 1), (5, 3), (5, 5).Sum of bit differences = 0 + 1 + 1 + 1 + 0 + 2 + 1 + 2 + 0 = 8</pre>

<b>Constraints:</b><br>1 ≤ n ≤ 10<sup>5<br></sup>1 ≤ arr[i] ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Bit Magic` `Data Structures`
- **Company Tags:** `Google`

### Related Articles
- [Sum Of Bit Differences Among All Pairs](https://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/)
