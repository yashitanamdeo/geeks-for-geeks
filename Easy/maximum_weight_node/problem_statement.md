<h1 align="center">Maximum Weight Node</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 53.85%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 32K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a maze with <b>n</b> cells. Each cell may have <b>multiple entry points</b> but <b>not more than one exit point</b> (i.e entry/exit points are unidirectional doors like valves).

You are given an array <b>exits[]</b>, where<b> exits[i] </b>contains the exit point of the ith cell.<br>If <b>exits[i]</b> is <b>-1,</b> then ith cell doesn't have an exit. 

The task is to find the cell with <b>maximum weight </b>(The <b>weight</b> of a cell <b>i</b> is the <b>sum of all the cell indexes</b> that have <b>exit point</b> as <b>i </b>). If there are multiple cells with the maximum weight return the cell with highest index.

<b>Note: </b>The cells are indexed with an integer value from 0 to n-1.<br>A cell <b>i</b> has <b>weight 0</b> if <b>no cell</b> has <b>exit point</b> as <b>i.</b>

<b><b>Examples:</b></b>

<pre><b><b>Input: </b></b>exits[] = [2, 0, -1, 2}<b>
<b>Output:</b> </b>2<b>
<b>Explanation</b>: 
</b>1 -> 0 -> 2 <- 3
weight of 0th cell = 1
weight of 1st cell = 0 (because there is no cell pointing to the 1st cell)
weight of 2nd cell = 0+3 = 3
weight of 3rd cell = 0
There is only one cell which has maximum weight (i.e 2)<br>So, cell 2 is the output.</pre>

<pre><b><b>Input: </b></b>exits[] = [-1]<b>
<b>Output:</b> </b>0<b>
<b>Explanation</b>:
</b>weight of 0<sup>th</sup> cell is 0.
There is only one cell so cell 0 has maximum weight.
</pre>

<b><b>Constraints:</b></b><br>1  ≤  n  ≤  10<sup>5</sup><br>-1  <u><</u>  exits[i]  <  N<br>exits[i]  ≠  i

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Graph` `Data Structures`
- **Company Tags:** `JUSPAY`

### Related Articles
- [Maximum Weight Node](https://www.geeksforgeeks.org/maximum-weight-node/)
