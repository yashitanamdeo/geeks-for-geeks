<h1 align="center">Maximum selections</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 69.52%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 5K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

<b>Note: This [POTD](http://practice.geeksforgeeks.org/problem-of-the-day) is a part of [Geek Summer Carnival](https://practice.geeksforgeeks.org/summer-carnival-2022?utm_source=potd&utm_medium=problempage&utm_campaign=gsc22). Solve all POTD consecutively from 5th to 10th April and get a chance to win exclusive discount vouchers on our GfG courses.</b>

<hr>
Geek wants to select the maximum number of course bundles at the Geek Summer Carnival. 

You are given a finite number of courses and N range of numbers each depicting a bundle of courses. Select the maximum number of bundles such that no courses overlap in any of the bundle.

<b>Note:</b> The ending of a range being the same as start of another isn't considered as an overlap.

<br>
<b>Example 1:</b>

<pre><b>Input:</b>
N = 4
Bundles = 
1 5
2 3
1 8
3 5

<b>Output:</b>
2

<b>Explanation: 
<img src="https://media.geeksforgeeks.org/img-practice/ScreenShot2022-04-01at4-1648812950.png" alt="" title=""/></b>
We can select 2 bundles at max while 
staying true to the condition. For this, 
we can pick the ranges (2,3) and (3,5) 
without any overlap. </pre>

 

<b>Example 2:</b>

<pre><b>Input:</b>
N = 5
Bundles = 
7 9 
2 8 
1 3 
10 11 
10 16

<b>Output:</b>
3

<b>Explanation: 
<img src="https://media.geeksforgeeks.org/img-practice/ScreenShot2022-04-01at4-1648813138.png" alt="" title=""/></b>
We can pick the ranges (1,3), 
(7,9) and (10,11) without any overlap.</pre>

<br>
<b>Your Task:</b><br>
You don't need to read input or print anything. Complete the function <b>max_non_overlapping()</b> that takes a 2D array representing N ranges as input parameter.  Return the maximum number of course bundles. 

<br>
<b>Expected time complexity: </b>O(NlogN)<br>
<b>Expected space complexity:</b> O(1)

<br>
<b>Constraints:</b><br>
1 <= N <= 1000<br>
0 <= range[i][j] <= 1000


<hr>

### Tags
- **Topic Tags:** `Sorting` `Algorithms`
- **Company Tags:** `None`
