<h1 align="center">Minimum K Consecutive Bit Flips</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Hard-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 64.29%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 9K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 8-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a binary array <b>arr[] </b>(containing only <b>0's</b> and <b>1's</b>) and an integer <b>k</b>. In one operation, you can select a contiguous subarray of length <b>k</b> and <b>flip all its bits</b> (i.e., change every 0 to 1 and every 1 to 0).

Your task is to find the <b>minimum </b>number of such operations required to make the entire array consist of only <b>1's</b>. If it is not possible, return <b>-1</b>.

<b>Examples:</b>

<pre><b>Input:</b> arr = [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1], k = 2<br><b>Output:</b> 4 <br><b>Explanation: </b>4 operations are required to convert all 0's to 1's.<br>Select subarray [2, 3] and flip all bits resulting array will be [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]<br>Select subarray [4, 5] and flip all bits resulting array will be [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1]<br>Select subarray [5, 6] and flip all bits resulting array will be [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1]<br>Select subarray [6, 7] and flip all bits resulting array will be [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]</pre>

<pre><b>Input:</b> arr = [0, 0, 1, 1, 1, 0, 0], k = 3<br><b>Output:</b> -1<br><b>Explanation:</b> It is not possible to convert all elements to 1's by performing any number of operations.</pre>

<b>Constraints:<br></b>1 ≤ arr.size() ≤ 10<sup>6</sup><br>1 ≤ k ≤ arr.size()

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(k)

<hr>

### Tags
- **Topic Tags:** `prefix-sum` `Bit Magic` `sliding-window` `Arrays` `Queue`
- **Company Tags:** `Bloomberg` `Amazon` `Facebook` `Microsoft` `Google`
