<h1 align="center">Count Special Numbers</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.46%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 41K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of positive integers <b>arr[]</b>. You need to find the count of the special numbers in arr[]. <br>A number is said to be a special number if it is divisible by atleast one <b>other </b>element of arr[]. 

<b>Examples :</b>

<pre><b>Input: </b>arr[] = [1, 2, 3]
<b>Output: </b>2
<b>Explanation: </b>2 and 3 are divible by 1.</pre>

<pre><b>Input: </b>arr[] = [2, 3, 4, 6, 8, 9]
<b>Output: </b>4<b><br></b><b>Explanation: </b>4, 6, 8 are divible by 2 and 9 is divisible by 3.</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>5 </sup><br>1 ≤ arr[i] ≤ 10<sup>6</sup><sup> </sup>

## Expected Complexities
- Time Complexity: O(n * sqrt(max(arr[i])))
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Mathematical` `sieve` `Data Structures` `Algorithms`
- **Company Tags:** `Intuit`

### Related Articles
- [Divisibility Check](https://www.geeksforgeeks.org/divisibility-check/)

### Related Interview Experiences
- [Intuit Interview Experience Set 13 Campus](https://www.geeksforgeeks.org/intuit-interview-experience-set-13-campus/)
