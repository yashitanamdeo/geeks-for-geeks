<h1 align="center">Taxi Booking</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 75.48%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 25K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are going to book a taxi. There are infinite number of points 1, 2, 3... on the X axis and your current position is <b>cur</b>. There are <b>N</b> Taxis near you, and the position of those taxis is given as an array <b>pos</b>. Where <b>pos[i]</b> denotes the position of the <b>ith</b> taxi. You are also given an array <b>time</b>. Where <b>time[i]</b> denotes the time taken by the <b>ith</b> taxi to cover <b>1 unit</b> of distance. Your task is to find the <b>minimum</b> time to board a taxi.

<b>Example 1:</b>

<pre><b>Input:</b>
N = 3, cur = 4
pos = [1, 5, 6]
time = [2, 3, 1]
<b>Output:</b>
2
<b>Explanation:</b>
Total time taken by the 1st taxi will be: (4-1)*2 = 6
Total time taken by the 2nd taxi will be: (5-4)*3 = 3
Total time taken by the 3rd taxi will be: (6-4)*1 = 2
So, the minimum time will be 2 sec.</pre>

 

<b>Example 2:</b>

<pre><b>Input:</b>
N = 2, cur = 1
pos = [1, 6]
time = [10, 3]
<b>Output:</b>
0
<b>Explanation:</b>
Total time taken by the 1st taxi will be: (1-1)*10 = 0
Total time taken by the 2nd taxi will be: (6-1)*3 = 15
So, the minimum time will be 0 sec.
</pre>

 

<b>Your Task:  </b><br>
You don't need to read input or print anything. Your task is to complete the function <b>minimumTime()</b> which takes two integers <b>N </b>and<b> cur</b>, and<b> 2</b> arrays <b>pos</b>, and<b> time </b>as input parameters and returns the minimum time required to board the taxi.

<b>Expected Time Complexity:</b> O(N)<br>
<b>Expected Auxiliary Space:</b> O(1)

<br>
<b>Constraints:</b><br>
1 ≤ N ≤ 10<sup>5</sup><br>
1 ≤ cur ≤ 10<sup>5</sup><br>
1 ≤ pos[i] ≤ 10<sup>5</sup><br>
1 ≤ time[i] ≤ 10<sup>3</sup>


<hr>

### Tags
- **Topic Tags:** `Arrays` `Greedy` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find Minimum Time To Board Taxi From Current Position](https://www.geeksforgeeks.org/find-minimum-time-to-board-taxi-from-current-position/)
