<h1 align="center">Count the number of possible triangles</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 28.53%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 149K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an integer array <b>arr[]</b>. Find the <b>number</b> of triangles that can be formed with <b>three </b>different array elements as lengths of three sides of the triangle. A triangle with three given sides is only possible if sum of any two sides is always <b>greater </b>than the third side.

<b>Examples:</b>

<pre><b>Input</b>: arr[] = [4, 6, 3, 7]
<b>Output</b>: 3
<b>Explanation</b>: There are three triangles possible [3, 4, 6], [4, 6, 7] and [3, 6, 7]. Note that [3, 4, 7] is not a possible triangle.  <br></pre>

<pre><b>Input</b>: arr[] = [10, 21, 22, 100, 101, 200, 300]
<b>Output</b>: 6
<b>Explanation</b>: There can be 6 possible triangles: [10, 21, 22], [21, 100, 101], [22, 100, 101], [10, 100, 101], [100, 101, 200] and [101, 200, 300].
</pre>

<pre><b>Input</b>: arr[] = [1, 2, 3]
<b>Output</b>: 0
<b>Explanation</b>: No triangles are possible.</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>3</sup><br>0 ≤ arr[i] ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n^2)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Sorting` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon` `Microsoft`

### Related Articles
- [Find Number Of Triangles Possible](https://www.geeksforgeeks.org/find-number-of-triangles-possible/)
