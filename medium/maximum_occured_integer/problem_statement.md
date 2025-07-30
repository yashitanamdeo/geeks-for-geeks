<h1 align="center">Maximum occured integer</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 32.93%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 93K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given two integer arrays <b>L[]</b> and <b>R[]</b>, where each <b>L[i]</b> and <b>R[i]</b> define the start and end of a range respectively. The goal is to find the integer that appears in the most number of these ranges. If multiple integers occur in the same maximum number of ranges, then return the smallest integer among them. <br>

<b>Examples :</b>

<pre><b>Input:</b> L[] = [1, 4, 3, 1], R[] = [15, 8, 5, 4]
<b>Output: </b>4<b>
Explanation: </b>The given ranges are [1, 15] [4, 8] [3, 5] [1, 4]. The smallest number that is most common or appears most times in the ranges is 4.
</pre>

<pre><b>Input: </b>L[] = [1, 5, 9, 13, 21], R[] = [15, 8, 12, 20, 30]
<b>Output: </b>5<b>
Explanation: </b>The given ranges are [1, 15] [5, 8] [9, 12] [13, 20] [21, 30]. The smallest number that is most common or appears most times in the ranges is 5.</pre>

<b>Constraints:</b><br>1 ≤ L.size() ≤ 10<sup>6</sup><br>0 ≤ L[i], R[i] ≤ 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n+max(R))
- Auxiliary Space: O(max(R))

<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures` `Mathematical` `Algorithms`
- **Company Tags:** `Amazon`

### Related Articles
- [Maximum Occurred Integer N Ranges](https://www.geeksforgeeks.org/maximum-occurred-integer-n-ranges/)
