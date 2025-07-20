<h1 align="center">Police and Thieves</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 34.03%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 45K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b>, where each element contains either a <b>'P'</b> for policeman or a <b>'T'</b> for thief. Find the <b>maximum number of thieves </b>that can be caught by the police. <br>Keep in mind the following conditions :

1. Each policeman can catch only one thief.
1. A policeman cannot catch a thief who is more than <b>k</b> units away from him.
<b>Examples:</b>

<pre><b>Input: </b>arr[] = ['P', 'T', 'T', 'P', 'T'], k = 1
<b>Output:</b> 2
<b>Explanation:</b> Maximum 2 thieves can be caught. First policeman catches first thief and second police man can catch either second or third thief.</pre>

<pre><b>Input: </b>arr[] = ['T', 'T', 'P', 'P', 'T', 'P'], k = 2
<b>Output:</b> 3
<b>Explanation: </b>Maximum 3 thieves can be caught.</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>5</sup><br>1 ≤ k ≤ 1000<br>arr[i] = 'P' or 'T'

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Greedy` `Algorithms` `two-pointer-algorithm`
- **Company Tags:** `Microsoft`

### Related Articles
- [Policemen Catch Thieves](https://www.geeksforgeeks.org/policemen-catch-thieves/)
