<h1 align="center">Equilibrium Point</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 28.13%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 649K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 15m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of integers<b> arr[]</b>,<b> </b>the task is to find the first <b>equilibrium point</b> in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before<b> </b>that index is the same as the sum<b> </b>of elements after<b> </b>it. Return -1 if no such point exists. 

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [1, 2, 0, 3]<br><b>Output: </b>2<b> 
Explanation: </b>The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.</pre>

<pre><b>Input: </b>arr[] = [1, 1, 1, 1]<br><b>Output: </b>-1<b>
Explanation: </b>There is no equilibrium index in the array.<br></pre>

<pre><b>Input: </b>arr[] = [-7, 1, 5, 2, -4, 3, 0]<br><b>Output: </b>3<b>
Explanation: </b>The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3 is -4 + 3 + 0 = -1.</pre>

<b>Constraints:</b><br>3 <= arr.size() <= 10<sup>5</sup><br>-10<sup>4</sup> <= arr[i] <= 10<sup>4</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `prefix-sum` `Arrays` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon` `Adobe` `Google` `Facebook` `Microsoft` `Uber`

### Related Articles
- [Equilibrium Index Of An Array](https://www.geeksforgeeks.org/equilibrium-index-of-an-array/)
