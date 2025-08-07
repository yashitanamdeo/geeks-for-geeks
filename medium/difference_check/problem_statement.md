<h1 align="center">Difference Check</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 72.79%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 4K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b> of time strings in 24-hour clock format <b>"HH:MM:SS"</b>, return the <b>minimum difference</b> in <b>seconds </b>between any two time strings in the arr[].<br>The clock wraps around at midnight, so the time difference between "23:59:59" and "00:00:00" is <b>1</b> second.

<b>Examples:<br></b>

<pre><b>Input: </b>arr[] = ["12:30:15", "12:30:45"]<b><br></b><b>Output: </b>30<b><br>Explanation:</b> The minimum time difference is 30 seconds.<b><br></b></pre>

<pre><b>Input: </b>arr[] = ["00:00:01", "23:59:59", "00:00:05"]<br><b>Output:</b> 2<b><br>Explanation: </b>The time difference is minimum between "00:00:01" and "23:59:59".<br></pre>

<b>Constraints:</b><br>2 ≤ arr.size() ≤ 10<sup>5</sup><br>arr[i] is in "HH:MM:SS" format.

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Strings` `Sorting`
- **Company Tags:** `None`

### Related Articles
- [Minimize Difference](https://www.geeksforgeeks.org/minimize-difference/)
