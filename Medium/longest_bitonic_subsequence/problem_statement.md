<h1 align="center">Longest Bitonic subsequence</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 47.34%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 131K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of positive integers. Find the <b>maximum</b> length of <b>Bitonic subsequence. </b><br>A subsequence of array is called Bitonic if it is first strictly increasing, then strictly decreasing. Return the maximum length of bitonic subsequence.<br> <br><b>Note</b> : A strictly increasing or a <b>strictly</b> decreasing sequence should not be considered as a bitonic sequence

<b>Examples :</b>

<pre><b>Input: </b>n = 5, nums[] = [1, 2, 5, 3, 2]
<b>Output: </b>5
<b>Explanation: </b>The sequence {1, 2, 5} is increasing and the sequence {3, 2} is decreasing so merging both we will get length 5.
</pre>

<pre><b>Input: </b>n = 8, nums[] = [1, 11, 2, 10, 4, 5, 2, 1]
<b>Output: </b>6
<b>Explanation: </b>The bitonic sequence {1, 2, 10, 4, 2, 1} has length 6.</pre>

<pre><b>Input: </b>n = 3, nums[] = [10, 20, 30]
<b>Output: </b>0
<b>Explanation: </b>The decreasing or increasing part cannot be empty</pre>

<pre><b>Input: </b>n = 3, nums[] = [10, 10, 10]
<b>Output: </b>0
<b>Explanation: </b>The subsequences must be strictly increasing or decreasing
</pre>

<b>Constraints:</b><br>1 ≤ length of array ≤ 10<sup>3</sup><br>1 ≤ arr[i] ≤ 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Microsoft` `Cisco`

### Related Articles
- [Longest Bitonic Subsequence Dp 15](https://www.geeksforgeeks.org/longest-bitonic-subsequence-dp-15/)

### Related Interview Experiences
- [Cisco Interview Experience Virtual Hiringon Campus For Internship 2020 21](https://www.geeksforgeeks.org/cisco-interview-experience-virtual-hiringon-campus-for-internship-2020-21/)
