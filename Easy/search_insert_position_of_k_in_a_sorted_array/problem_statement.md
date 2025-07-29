<h1 align="center">Search insert position of K in a sorted array</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 38.99%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 81K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given a sorted array <b>arr[] </b>(0-index based) of distinct integers and an integer <b>k</b>, find the <b>index </b>of k if it is present in the arr[]. If not, return the <b>index </b>where k should be inserted to maintain the <b>sorted order</b>.

<b>Examples :</b>

<pre><b>Input: </b>arr[] = [1, 3, 5, 6], k = 5<b>
Output: </b>2<b>
Explanation: </b>Since 5 is found at index 2 as arr[2] = 5, the output is 2.</pre>

<pre><b>Input: </b>arr[] = [1, 3, 5, 6], k = 2<b>
Output: </b>1<b>
Explanation: </b>The element 2 is not present in the array, but inserting it at index 1 will maintain the sorted order.</pre>

<pre><b>Input:</b> arr[] = [2, 6, 7, 10, 14], k = 15<br><b>Output:</b> 5<br><b>Explanation:</b> The element 15 is not present in the array, but inserting it after index 4 will maintain the sorted order.</pre>

<b>Constraints:<br></b>1 ≤ arr.size() ≤ 10<sup>4</sup><br>-10<sup>3</sup> ≤ arr[i] ≤ 10<sup>3</sup><br>-10<sup>3</sup> ≤ k ≤ 10<sup>3</sup>

## Expected Complexities
- Time Complexity: O(log n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Searching` `Algorithms`
- **Company Tags:** `Microsoft`

### Related Articles
- [Search Insert Position Of K In A Sorted Array](https://www.geeksforgeeks.org/search-insert-position-of-k-in-a-sorted-array/)
