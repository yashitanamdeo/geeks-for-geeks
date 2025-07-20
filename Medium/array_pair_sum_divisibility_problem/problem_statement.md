<h1 align="center">Array Pair Sum Divisibility Problem</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 27.85%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 133K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of integers <b>nums</b> and a number <b>k</b>, write a function that returns <b>true </b>if given array can be divided into pairs such that sum of every pair is divisible by <b>k</b>.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [9, 5, 7, 3], k = 6
<b>Output: </b>true
<b>Explanation: </b>{(9, 3), (5, 7)} is a possible solution. 9 + 3 = 12 is divisible by 6 and 7 + 5 = 12 is also divisible by 6.
</pre>

<pre><b>Input:</b> arr[] = [4, 4, 4], k = 4
<b>Output: </b>false
<b>Explanation: </b>You can make 1 pair at max, leaving a single element unpaired.
</pre>

<pre><b>Input: </b>arr[]<b> </b>= [4, 4], k = 4
<b>Output: </b>true
<b>Explanation: </b>Here only {(4,4)} is possible whose sum 4 + 4 = 8 is divisible by 4.</pre>

<b>Constraints:</b><br>1 <= arr.size() <= 10<sup>5</sup><br>1 <= arr[i] <= 10<sup>5</sup><br>1 <= k <= 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Hash` `STL` `Data Structures`
- **Company Tags:** `Amazon` `Microsoft` `Goldman Sachs` `Directi`

### Related Articles
- [Check If An Array Can Be Divided Into Pairs Whose Sum Is Divisible By K](https://www.geeksforgeeks.org/check-if-an-array-can-be-divided-into-pairs-whose-sum-is-divisible-by-k/)

### Related Interview Experiences
- [Directi Interview Set 8 Off Campus](https://www.geeksforgeeks.org/directi-interview-set-8-off-campus/)
