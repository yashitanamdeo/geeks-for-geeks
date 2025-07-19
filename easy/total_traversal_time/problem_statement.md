<h1 align="center">Total Traversal Time</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.0%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 33K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given two arrays arr[ ] and penalty[ ], each of size n.<br>All elements in arr[ ] are in the range of 1 to n. You have to traverse arr[ ] from start to end while following the given conditions.

1. If element has never occured before, it takes 1 second to move a step ahead.
1. If element has occured before, it will take penalty[arr[i]] seconds to move a step. Here i is the index of current element with 1-based indexing.
Find the total time taken to traverse through the array.

<b>Example 1:</b>

<pre><b>Input:</b>
n = 4
arr[ ] = {1, 2, 3, 3}
penalty[ ] = {1, 2, 3, 4}
<b>Output: </b>5
<b>Explanation:
</b>

For i = 1, traversal time = 0 second since this is the start point.  
For i = 2, traversal time = 1 second 
For i = 3, traversal time = 1 second 
For i = 4, traversal time = penalty[arr[4]]  = penalty[3] = 3
Total = 0+1+1+3 = 5 </pre>

<b>Example 2:</b>

<pre><b>Input:</b>
n = 8
arr = {6, 6, 1, 8, 1, 1, 3, 1}
time ={8, 4, 1, 5, 2, 8, 9, 3}<b>
Output:</b>
35<b>
Explanation:
</b>
</pre>

<b>Your Task:</b><br>You don't need to read input or print anything. Your task is to complete the function totalTime() which takes three input parameters n, arr[ ], penalty[ ] and returns the total time taken to traverse through the array. <br><br><b>Expected Time Complexity:</b> O(n)<br><b>Expected Auxiliary Space:</b> O(n)<br><br><b>Constraints:</b><br>1 <= n <= 10^5<br>1 <= arr[i] <= n<br>1 <= time[i] <= 10^5


<hr>

### Tags
- **Topic Tags:** `Arrays` `Hash` `Data Structures`
- **Company Tags:** `None`
