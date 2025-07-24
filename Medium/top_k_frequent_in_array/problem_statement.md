<h1 align="center">Top K Frequent in Array</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 40.23%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 97K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a non-empty integer array <b>arr[]</b> of size n, find the top <b>k</b> elements which have the <b>highest frequency </b>in the array. 

Note: If two numbers have the same frequencies, then the <b>larger number </b>should be given more preference.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [3, 1, 4, 4, 5, 2, 6, 1], k = 2<br><b>Output: </b>[4, 1]<br><b>Explanation: </b>Frequency of 4 is 2 and frequency of 1 is 2, these two have the maximum frequency and 4 is larger than 1.</pre>

<pre><b>Input: </b>arr[] = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], k = 4<br><b>Output: </b>[5, 11, 7, 10]<b>
Explanation: </b>Frequency of 5 is 3, frequency of 11 is 2, frequency of 7 is 2, frequency of 10 is 1.</pre>

<b>Constraints: </b><br>1 <= n <= 10<sup>5</sup><br>1<= arr[i] <=10<sup>5<br></sup>1 <= k <= no. of distinct elements

## Expected Complexities
- Time Complexity: O(n log n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Hash` `Sorting` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon` `Microsoft`

### Related Articles
- [Find K Numbers Occurrences Given Array](https://www.geeksforgeeks.org/find-k-numbers-occurrences-given-array/)
