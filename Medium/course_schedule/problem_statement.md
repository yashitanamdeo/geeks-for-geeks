<h1 align="center">Course Schedule</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 51.77%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 82K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 25m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

There are a total of <b>n</b> tasks you have to pick, labelled from <b>0 to n-1</b>. Some tasks may have <b>prerequisites[][] </b>tasks, for example to pick task <b>0</b> you have to first finish tasks <b>1</b>, which is expressed as a pair: <b>[0, 1]</b><br>Given the total number of <b>n</b> tasks and a list of prerequisite pairs of size <b>m</b>. Find a ordering of tasks you should pick to finish all tasks.<br><b>Note: </b>There may be multiple correct orders, you just need to return any one of them. If it is impossible to finish all tasks, return an empty array. Returning any correct order will give the output as <b>true</b>, whereas any invalid order will give the output <b>false</b>. 

<b>Examples:</b>

<pre><b>Input: </b>n = 2, prerequisites[][] = [[1, 0]]
<b>Output: </b>true<b>
Explanation: </b>Only possible order is [0, 1].</pre>

<pre><b>Input: </b>n = 4, prerequisites[][] = [[1, 0], [2, 0], [3, 1], [3, 2]]
<b>Output: </b>true<b>
Explanation: </b>There are a total of 4 tasks to pick. To pick task 3 you should have finished both tasks 1 and 2. Both tasks 1 and 2 should be pick after you finished task 0. So one correct task order is [0, 1, 2, 3]. Another correct ordering is [0, 2, 1, 3]. Returning any of these order will result in an output of true.
</pre>

<b>Constraints:</b><br>1 ≤ n ≤ 10<sup>5</sup>
0 ≤ prerequisites[i][0], prerequisites[i][1] < n<br>All prerequisite pairs are unique
prerequisites[i][0] ≠ prerequisites[i][1]

## Expected Complexities
- Time Complexity: O(n + m)
- Auxiliary Space: O(n + m)

<hr>

### Tags
- **Topic Tags:** `DFS` `Graph` `BFS` `Data Structures` `Algorithms`
- **Company Tags:** `Google`

### Related Articles
- [Find Course Schedule Ii](https://www.geeksforgeeks.org/find-course-schedule-ii/)
- [Find Whether It Is Possible To Finish All Tasks Or Not From Given Dependencies](https://www.geeksforgeeks.org/find-whether-it-is-possible-to-finish-all-tasks-or-not-from-given-dependencies/)
