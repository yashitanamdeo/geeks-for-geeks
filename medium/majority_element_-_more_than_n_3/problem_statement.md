<h1 align="center">Majority Element - More Than n/3</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 48.1%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 184K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr</b><b>[]</b> consisting of <b>n</b> integers, the task is to find all the array elements which occurs more than floor(n/3) times.

<b>Note: </b>The returned array of majority elements should be sorted.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [2, 2, 3, 1, 3, 2, 1, 1]
<b>Output: </b>[1, 2]
<b>Explanation: </b>The frequency of 1 and 2 is 3, which is more than floor n/3 (8/3 = 2).</pre>

<pre><b>Input: </b> arr[] = [-5, 3, -5]
<b>Output: </b>[-5]<br><b>Explanation: </b>The frequency of -5 is 2, which is more than floor n/3 (3/3 = 1).<br></pre>

<pre><b>Input: </b> arr[] = [3, 2, 2, 4, 1, 4]<b><br>Output: </b>[]<b><br>Explanation: </b>There is no majority element.</pre>

<b>Constraint:</b><br>1 ≤ arr.size() ≤ 10<sup>6</sup><br>-10<sup>5</sup> ≤ arr[i] ≤ 10<sup>5</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures` `Algorithms` `Hash`
- **Company Tags:** `Bloomberg` `Salesforce` `Accenture` `Microsoft` `TCS` `Google`

### Related Articles
- [Candidates With Majority Vote](https://www.geeksforgeeks.org/candidates-with-majority-vote/)
