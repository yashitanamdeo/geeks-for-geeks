<h1 align="center">First and Last Occurrences</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 37.36%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 290K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a sorted array <b>arr</b> with possibly some duplicates, the task is to find the first and last occurrences of an element <b>x</b> in the given array.<br><b>Note:</b> If the number <b>x</b> is not found in the array then return both the indices as -1.<br>

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [1, 3, 5, 5, 5, 5, 67, 123, 125], x = 5
<b>Output: </b>[2, 5]
<b>Explanation</b>: First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5
</pre>

<pre><b>Input: </b>arr[] = [1, 3, 5, 5, 5, 5, 7, 123, 125], x = 7
<b>Output:</b> [6, 6]<br><b>Explanation:</b> First and last occurrence of 7 is at index 6<br></pre>

<pre><b>Input: </b>arr[] = [1, 2, 3], x = 4
<b>Output:</b> [-1, -1]
<b>Explanation</b>: No occurrence of 4 in the array, so, output is [-1, -1]</pre>

<b>Constraints:<br></b>1 ≤ arr.size() ≤ 10<sup>6</sup><br>1 ≤ arr[i], x ≤ 10<sup>9</sup><br>

## Expected Complexities
- Time Complexity: O(log n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Binary Search` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon`

### Related Articles
- [Find First And Last Positions Of An Element In A Sorted Array](https://www.geeksforgeeks.org/find-first-and-last-positions-of-an-element-in-a-sorted-array/)

### Related Interview Experiences
- [Amazon Interview Experience Set 416 Campus Internship](https://www.geeksforgeeks.org/amazon-interview-experience-set-416-campus-internship/)
