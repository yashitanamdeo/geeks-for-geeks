<h1 align="center">Game with String</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.96%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 70K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a string <b>s</b> consisting of lowercase alphabets and an integer <b>k,</b> your task is to find the <b>minimum </b>possible value of the string after removing exactly <b>k</b> characters.

The <b>value </b>of the string is defined as the <b>sum </b>of the squares of the frequencies of each distinct character present in the string.

<b>Examples :</b>

<pre><b>Input:</b> s = "abbccc", k = 2
<b>Output:</b> 6
<b>Explaination: </b>We remove two 'c' to get the value as 1<sup>2</sup> + 2<sup>2</sup> + 1<sup>2</sup> = 6 or We remove one 'b' and one 'c' to get the value 1<sup>2</sup> + 1<sup>2</sup> + 2<sup>2</sup> = 6.</pre>

<pre><b>Input: </b>s = "aaab", k = 2
<b>Output:</b> 2
<b>Explaination:</b> We remove two 'a'. Now we get the value as 1<sup>2 </sup>+ 1<sup>2</sup> = 2.</pre>

<b>Constraints:</b><br>0 ≤ k ≤ s.length() ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Strings` `Heap` `Data Structures`
- **Company Tags:** `Amazon`

### Related Articles
- [Minimum Sum Squares Characters Counts Given String Removing K Characters](https://www.geeksforgeeks.org/minimum-sum-squares-characters-counts-given-string-removing-k-characters/)
