<h1 align="center">Rearrange an array with O(1) extra space</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 56.34%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 121K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array <b>arr[]</b> of size <b>n</b> where every element is in the range from <b>0 to n-1</b>. Rearrange the given array so that the transformed array <b>arr<sup>T</sup>[i]</b> becomes <b>arr[arr[i]]</b>.<br><b>NOTE:</b> <b>arr </b>and <b>arr<sup>T</sup> </b>are both same variables, representing the array before and after transformation respectively.

<b>Examples:<br></b>

<pre><b>Input:</b> arr[] = [1,0]
<b>Output: [</b>0, 1]<b>
Explanation: </b>arr[arr[0]] = arr[1] = 0, arr[arr[1]] = arr[0] = 1 So, arr<sup>T</sup> becomes [0, 1]
</pre>

<pre><b>Input:</b> arr[] = [4,0,2,1,3]
<b>Output: [</b>3, 4, 2, 0, 1]<b>
Explanation: </b>arr[arr[0]] = arr[4] = 3, arr[arr[1]] = arr[0] = 4, arr[arr[2]] = arr[2] = 2, arr[arr[3]] = arr[1] = 0, arr[arr[4]] = arr[3] = 1 and so on So, arr<sup>T</sup> becomes [3, 4, 2, 0, 1]</pre>

<b>Constraints:</b><br>1 ≤ n ≤ 10<sup>5</sup><br>0 ≤ arr[i] < n

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Data Structures` `Algorithms`
- **Company Tags:** `Amazon`

### Related Articles
- [Rearrange Given Array Place](https://www.geeksforgeeks.org/rearrange-given-array-place/)
