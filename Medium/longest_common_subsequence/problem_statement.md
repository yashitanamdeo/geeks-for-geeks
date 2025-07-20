<h1 align="center">Longest Common Subsequence</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 41.68%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 316K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two strings <b>s1</b> and <b>s2</b>, return the length of their <b>longest common subsequence </b>(LCS). If there is no common subsequence, return <b>0</b>.

<i>A subsequence is a sequence that can be derived from the given string by deleting some or no elements without changing the order of the remaining elements. For example, "ABE" is a subsequence of "ABCDE".</i>

<b>Examples:</b>

<pre><b>Input: </b>s1 = "ABCDGH", s2 = "AEDFHR"
<b>Output: </b>3<b>
Explanation: </b>The longest common subsequence of "ABCDGH" and "AEDFHR" is "ADH", which has a length of 3.
</pre>

<pre><b>Input: </b>s1 = "ABC", s2 = "AC"
<b>Output: </b>2<b>
Explanation: </b>The longest common subsequence of "ABC" and "AC" is "AC", which has a length of 2.</pre>

<pre><b>Input: </b>s1 = "XYZW", s2 = "XYWZ"
<b>Output: </b>3<b>
Explanation: </b>The longest common subsequences of "XYZW" and "XYWZ" are "XYZ" and "XYW", both of length 3.</pre>

<b>Constraints:</b><br>1<= s1.size(), s2.size() <=10<sup>3<br></sup>Both strings s1 and s2 contain only uppercase English letters.

## Expected Complexities
- Time Complexity: O(n * m)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Dynamic Programming` `Algorithms`
- **Company Tags:** `Paytm` `VMWare` `Amazon` `Microsoft` `Citrix` `MakeMyTrip`

### Related Articles
- [Longest Common Subsequence Dp 4](https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/)
- [Space Optimized Solution Lcs](https://www.geeksforgeeks.org/space-optimized-solution-lcs/)

### Related Interview Experiences
- [Vmware Interview Experience Set 8 Campus Mts Propel Program](https://www.geeksforgeeks.org/vmware-interview-experience-set-8-campus-mts-propel-program/)
- [Makemytrip Interview Experience Set 7 On Campus](https://www.geeksforgeeks.org/makemytrip-interview-experience-set-7-on-campus/)
