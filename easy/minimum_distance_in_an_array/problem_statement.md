<h1 align="center">Minimum distance in an Array</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 19.75%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 246K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given an array, <b>arr[]</b>. Find the <b>minimum </b>index based distance between two distinct elements of the array, <b>x</b> and <b>y</b>. Return -1, if either <b>x </b>or <b>y </b>does not exist in the array.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [1, 2, 3, 2], x = 1, y = 2
<b>Output: </b>1<b>
Explanation: </b>x = 1 and y = 2. There are two distances between x and y, which are 1 and 3 out of which the least is 1.
</pre>

<pre><b>Input: </b>arr[] = [86, 39, 90, 67, 84, 66, 62], x = 42, y = 12
<b>Output: </b>-1<b>
Explanation: </b>x = 42 and y = 12. We return -1 as x and y don't exist in the array.</pre>

<pre><b>Input: </b>arr[] = [10, 20, 30, 40, 50], x = 10, y = 50
<b>Output: </b>4<b>
Explanation: </b>The distance between x = 10 (index 0) and y = 50 (index 4) is 4, which is the only distance between them.</pre>

<b>Constraints:</b><br>1 <= arr.size() <= 10<sup>5</sup><br>0 <= arr[i], x, y <= 10<sup>5<br></sup>x != y

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures`
- **Company Tags:** `Paytm` `Amazon`

### Related Articles
- [Find The Minimum Distance Between Two Numbers](https://www.geeksforgeeks.org/find-the-minimum-distance-between-two-numbers/)

### Related Interview Experiences
- [Paytm Interview Experience Set 4 Walk In Drive](https://www.geeksforgeeks.org/paytm-interview-experience-set-4-walk-in-drive/)
- [Paytm Interview Experience Set 10 Experienced](https://www.geeksforgeeks.org/paytm-interview-experience-set-10-experienced/)
