<h1 align="center">Find H-Index</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.4%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 51K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array <b>citations[],</b> where each element <b>citations[i]</b> represents the number of <b>citations</b> received by the <b>i<sup>th</sup></b> paper of a researcher. You have to calculate the researcher’s <b>H</b><b>-index</b>.<br>The <b>H-index</b> is defined as the maximum value <b>H</b>, such that the researcher has published at least <b>H papers</b>, and all those papers have <b>citation value</b> greater than or equal to <b>H</b>.

<b>Examples:</b>

<pre><b>Input: </b>citations[] = [3, 0, 5, 3, 0]<br><b>Output:</b> 3<br><b>Explanation:</b> There are at least 3 papers with citation counts of 3, 5, and 3, all having citations greater than or equal to 3.</pre>

<pre><b>Input:</b> citations[] = [5, 1, 2, 4, 1]<br><b>Output:</b> 2<br><b>Explanation:</b> There are 3 papers (with citation counts of 5, 2, and 4) that have 2 or more citations. However, the H-Index cannot be 3 because there aren't 3 papers with 3 or more citations.<br></pre>

<pre><b>Input:</b> citations[] = [0, 0]<br><b>Output:</b> 0<br><b>Explanation:</b> The H-index is 0 because there are no papers with at least 1 citation.</pre>

<b>Constraints:</b><br>1 ≤ citations.size() ≤ 10<sup>6<br></sup>0 ≤ citations[i] ≤ 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Sorting` `Arrays` `Binary Search`
- **Company Tags:** `None`

### Related Articles
- [What Is H Index](https://www.geeksforgeeks.org/what-is-h-index/)
