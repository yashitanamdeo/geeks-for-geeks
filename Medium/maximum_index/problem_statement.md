<h1 align="center">Maximum Index</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 13.46%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 216K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array,<b> arr[] </b>of<b> </b>non-negative integers. The task is to return the maximum of <b>j - i (i<=j)</b> subjected to the constraint of <b>arr[i] <= arr[j]</b>.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [34, 8, 10, 3, 2, 80, 30, 33, 1]<br><b>Output: </b>6<br><b>Explanation: </b>In the given array arr[1] < arr[7] satisfying the required condition (arr[i] <= arr[j]) thus giving the maximum difference of j - i which is 7-1 = 6.</pre>

<pre><b>Input: </b>arr[] = [18, 17]<br><b>Output: </b>0<br><b>Explanation:</b> We can either take i and j as 0 and 0 or we cantake 1 and 1 both give the same result 0.</pre>

<pre><b>Input: </b>arr[] = [10, 10, 10, 10]<br><b>Output: </b>3<br><b>Explanation:</b> Since all elements are equal, any pair of indices will satisfy the condition arr[i] <= arr[j]. The maximum difference is between j = 3 and i = 0, resulting in j - i = 3.</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>6</sup><br>0 ≤ arr[i] ≤ 10<sup>9</sup>

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(n)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures`
- **Company Tags:** `VMWare` `Amazon` `Snapdeal` `Google`

### Related Articles
- [Given An Array Arr Find The Maximum J I Such That Arrj Arri](https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/)

### Related Interview Experiences
- [Vmware Interview Set 1 For Mts 2 Position](https://www.geeksforgeeks.org/vmware-interview-set-1-for-mts-2-position/)
