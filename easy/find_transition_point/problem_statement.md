<h1 align="center">Find Transition Point</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 37.9%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 277K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 20m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a <b>sorted array, arr[] </b>containing only <b>0s </b>and <b>1s</b>, find the <b>transition point</b>, i.e., the <b>first index </b>where <b>1 </b>was observed, and <b>before that</b>, only 0 was observed.  If <b>arr</b> does not have any <b>1</b>, return <b>-1</b>. If array does not have any <b>0</b>, return <b>0</b>.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [0, 0, 0, 1, 1]
<b>Output:</b> 3
<b>Explanation:</b> index 3 is the transition point where 1 begins.</pre>

<pre><b>Input: </b>arr[] = [0, 0, 0, 0]
<b>Output:</b> -1
<b>Explanation:</b> Since, there is no "1", the answer is -1.<br></pre>

<pre><b>Input: </b>arr[] = [1, 1, 1]
<b>Output:</b> 0
<b>Explanation:</b> There are no 0s in the array, so the transition point is 0, indicating that the first index (which contains 1) is also the first position of the array.</pre>

<pre><b>Input: </b>arr[] = [0, 1, 1]
<b>Output:</b> 1
<b>Explanation:</b> Index 1 is the transition point where 1 starts, and before it, only 0 was observed.</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>5</sup><br>0 ≤ arr[i] ≤ 1

## Expected Complexities
- Time Complexity: O(log n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Searching` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon`

### Related Articles
- [Find Transition Point Binary Array](https://www.geeksforgeeks.org/find-transition-point-binary-array/)

### Related Interview Experiences
- [Amazon Interview Set 86 Sde](https://www.geeksforgeeks.org/amazon-interview-set-86-sde/)
