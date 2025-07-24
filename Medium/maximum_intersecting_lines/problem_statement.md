<h1 align="center">Maximum Intersecting Lines</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.99%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 25K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

<b>N </b>horizontal line segments are arranged on the X-axis of a 2D plane. The start and end point of each line segment is given in a <b>Nx2</b> matrix <b>lines[ ][ ]</b>. Your task is to find the maximum number of intersections possible of any vertical line with the given <b>N </b>line segments.

<b>Example 1:</b>

<pre><b>Input:</b>
N = 4
lines[][] = {{1,3}, {2,3}, {1,2}, {4,4}}
<b>Output:</b>
3
<b>Explanation:</b>
A vertical line at X = 2 passes through 
{1,3}, {2,3}, {1,2}, ie three of the 
given horizontal lines.</pre>

<b>Example 2:</b>

<pre><b>Input: </b>
N = 3
lines[][] = {{1, 3}, {5, 6}, {3,4}}
<b>Output:</b>
2
<b>Explanation: 
</b>A vertical line at X = 3 passes through 
two of the given horizontal lines which 
is the maximum possible.
</pre>

<b>Your Task:</b><br>
You dont need to read input or print anything. Complete the function <b>maxIntersections</b><b>() </b>which takes the 2D Matrix <b>lines[][] </b>and the integer <b>N</b> as input parameters, and returns the maximum intersections possible.

<b>Expected Time Complexity:</b> O(N*log(N))<br>
<b>Expected Auxiliary Space:</b> O(N)

<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>5 </sup><br>
-10<sup>9 </sup>≤ lines[i][0] ≤ 10<sup>9</sup><br>
lines[i][0] ≤ lines[i][1] ≤ 10<sup>9</sup>


<hr>

### Tags
- **Topic Tags:** `Mathematical` `Sorting` `Geometric` `Algorithms`
- **Company Tags:** `Swiggy`

### Related Articles
- [Find The Maximum Number Of Intersections Lines](https://www.geeksforgeeks.org/find-the-maximum-number-of-intersections-lines/)
