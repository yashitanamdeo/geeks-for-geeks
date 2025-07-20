<h1 align="center">Array Leaders</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 29.94%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 897K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array <b>arr</b> of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.

<b>Examples:<br></b>

<pre><b>Input: </b>arr = [16, 17, 4, 3, 5, 2]
<b>Output: </b>[17, 5, 2]<b>
Explanation: </b>Note that there is nothing greater on the right side of 17, 5 and, 2.
</pre>

<pre><b>Input: </b>arr = [10, 4, 2, 4, 1]
<b>Output: </b>[10, 4, 4, 1]<br><b>Explanation:</b> Note that both of the 4s are in output, as to be a leader an equal element is also allowed on the right. side</pre>

<pre><b>Input: </b>arr = [5, 10, 20, 40]<br><b>Output: </b>[40]<br><b>Explanation:</b> When an array is sorted in increasing order, only the rightmost element is leader.</pre>

<pre><b>Input: </b>arr = [30, 10, 10, 5]<br><b>Output:</b> [30, 10, 10, 5]<br><b>Explanation:</b> When an array is sorted in non-increasing order, all elements are leaders.</pre>

<b>Constraints:</b><br>1 <= arr.size() <= 10<sup>6</sup><br>0 <= arr[i] <= 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures`
- **Company Tags:** `Payu` `Adobe`

### Related Articles
- [Leaders In An Array](https://www.geeksforgeeks.org/leaders-in-an-array/)

### Related Interview Experiences
- [Adobe Interview Experience Shecodes Software Engineer](https://www.geeksforgeeks.org/adobe-interview-experience-shecodes-software-engineer/)
