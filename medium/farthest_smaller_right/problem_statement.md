<h1 align="center">Farthest Smaller Right</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 50.08%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 16K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array <b>arr[]</b>. For each element at index i (0-based indexing), find the <b>farthest index </b>j to the right (i.e., j > i) such that arr[j] < arr[i]. If no such index exists for a given position, return <b>-1 </b>for that index. Return the resulting array of answers.

<b>Examples:</b>

<pre><b><b>Input: </b></b>arr[] = [2, 5, 1, 3, 2]<br><b><b>Output:</b></b> [2, 4, -1, 4, -1]<br><b><b>Explanation:</b></b> arr[0] = 2: Farthest smaller element to the right is arr[2] = 1.<br>arr[1] = 5: Farthest smaller element to the right is arr[4] = 2.<br>arr[2] = 1: No smaller element to the right → -1.<br>arr[3] = 3: Farthest smaller element to the right is arr[4] = 2.<br>arr[4] = 2: No elements to the right → -1.</pre>

<pre><b><b>Input:</b></b> arr[] = [2, 3, 5, 4, 1] <br><b><b>Output:</b></b> [4, 4, 4, 4, -1]<br><b><b>Explanation: </b></b>arr[4] is the farthest smallest element to the right for arr[0], arr[1], arr[2] and arr[3].<br></pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>6<br></sup>1 ≤ arr[i] ≤ 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n log n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Binary Search` `Arrays` `Data Structures` `Algorithms`
- **Company Tags:** `None`

### Related Articles
- [Find The Farthest Smaller Number In The Right Side](https://www.geeksforgeeks.org/find-the-farthest-smaller-number-in-the-right-side/)
