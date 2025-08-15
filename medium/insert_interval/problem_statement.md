<h1 align="center">Insert Interval</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.61%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 52K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Geek has an array of non-overlapping intervals <b>intervals[][]</b> where <b>intervals[i]</b> = <b>[start<sub>i </sub>, end<sub>i</sub>]</b> represent the start and the end of the <b>i<sup>th</sup></b> event and intervals is sorted in <b>ascending</b> order by <b>start<sub>i </sub></b>. He wants to add a new interval <b>newInterval[] </b>=<b> [newStart, newEnd]</b> where newStart and newEnd represent the start and end of this interval.<br>Help Geek to <b>insert </b>newInterval into intervals such that intervals is still sorted in ascending order by <b>start<sub>i</sub></b> and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

<b>Examples:</b>

<pre><b>Input: </b>intervals[][] = [[1, 3], [4, 5], [6, 7], [8, 10]], newInterval[] = [5, 6]
<b>Output: </b>[[1, 3], [4, 7], [8, 10]]
<b>Explanation: </b>The newInterval [5, 6] overlaps with [4, 5] and [6, 7]. So, they are merged into one interval [4, 7].
</pre>

<pre><b>Input: </b>intervals[][] = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval[] = [4, 9]
<b>Output: </b>[[1, 2], [3, 10], [12, 16]]
<b>Explanation: </b>The new interval [4, 9] overlaps with [3, 5], [6, 7] and [8, 10]. So, they are merged into one interval [3, 10].</pre>

<b>Constraints:</b><br>1 ≤ intervals.size() ≤  10<sup>5</sup><br>0 ≤ start<sub>i</sub> ≤ end<sub>i</sub> ≤ 10<sup>9</sup><br>0 ≤ newStart ≤ newEnd ≤ 10<sup>9</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Sorting` `Greedy` `Arrays`
- **Company Tags:** `None`

### Related Articles
- [Insert In Sorted And Non Overlapping Interval Array](https://www.geeksforgeeks.org/insert-in-sorted-and-non-overlapping-interval-array/)
