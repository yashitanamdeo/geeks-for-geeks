<h1 align="center">Next element with greater frequency</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 60.4%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 23K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[] </b>of integers, for each element, find the closest (distance wise) to its <b>right</b> that has a <b>higher frequency </b>than the current element.<br> If no such element exists, return <b>-1</b> for that position.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [2, 1, 1, 3, 2, 1]<b><br>Output: </b>[1, -1, -1, 2, 1, -1]<b><br>Explanation: </b>Frequencies: 1 → 3 times, 2 → 2 times, 3 → 1 time.<br>For arr[0] = 2, the next element 1 has a higher frequency → 1.
For arr[1] and arr[2], no element to the right has a higher frequency → -1.
For arr[3] = 3, the next element 2 has a higher frequency → 2.
For arr[4] = 2, the next element 1 has a higher frequency → 1.
For arr[5] = 1, no elements to the right → -1.</pre>

<pre><b>Input:</b> arr[] = [5, 1, 5, 6, 6]<br><b>Output:</b> [-1, 5, -1, -1, -1]<br><b>Explanation: </b>Frequencies: 1 → 1 time, 5 → 2 times, 6 → 2 times.<br>For arr[0] and arr[2], no element to the right has a higher frequency → -1.<br>For arr[1] = 1, the next element 5 has a higher frequency → 5.<br>For arr[3] and arr[4], no element to the right has a higher frequency → -1.</pre>

<b>Constraints:<br></b>1 ≤ arr.size() ≤ 10<sup>5<sub><br></sub></sup>1 ≤ arr[i] ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Hash` `Stack` `Data Structures`
- **Company Tags:** `None`

### Related Articles
- [Next Greater Frequency Element](https://www.geeksforgeeks.org/next-greater-frequency-element/)
