<h1 align="center">Max Sum Subarray of size K</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Easy-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 49.6%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 201K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 2-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: N/A-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

Given an array of integers<b> arr[] </b> and a number<b> k</b>. Return the <b>maximum sum</b> of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

<b>Examples:</b>

<pre><b>Input:</b> arr[] = [100, 200, 300, 400] , k = 2
<b>Output: </b>700
<b>Explanation: </b>arr<sub>3 </sub> + arr<sub>4</sub> = 700, which is maximum.</pre>

<pre><b>Input: </b>arr[] = [100, 200, 300, 400] , k = 4
<b>Output: </b>1000
<b>Explanation: </b>arr<sub>1</sub> + arr<sub>2</sub> + arr<sub>3 </sub>+ arr<sub>4</sub> = 1000, which is maximum.<br></pre>

<pre><b>Input:</b> arr[] = [100, 200, 300, 400] , k = 1
<b>Output: </b>400
<b>Explanation: </b>arr<sub>4</sub> = 400, which is maximum.</pre>

<b>Constraints:</b><br>1 <= arr.size() <= 10<sup>6<br></sup>1 <= arr[i]<= 10<sup>6<br></sup>1 <= k<= arr.size()

## Expected Complexities
- Time Complexity: O(n)
- Auxiliary Space: O(1)

<hr>

### Tags
- **Topic Tags:** `prefix-sum` `sliding-window` `Misc` `Algorithms`
- **Company Tags:** `OYO Rooms`

### Related Articles
- [Find Maximum Minimum Sum Subarray Size K](https://www.geeksforgeeks.org/find-maximum-minimum-sum-subarray-size-k/)
- [Window Sliding Technique](https://www.geeksforgeeks.org/window-sliding-technique/)
