<h1 align="center">K closest elements</h1>

<p align="center">
  <img alt="Difficulty" title="Difficulty" src="https://custom-icon-badges.demolab.com/badge/Difficulty: Medium-1F222E?style=for-the-badge&logoColor=white&logo=fire"/>
  <img alt="Accuracy" title="Accuracy" src="https://custom-icon-badges.demolab.com/badge/Accuracy: 15.96%25-1F222E?style=for-the-badge&logoColor=white&logo=target"/>
  <img alt="Submissions" title="Submissions" src="https://custom-icon-badges.demolab.com/badge/Submissions: 88K+-1F222E?style=for-the-badge&logoColor=white&logo=repo"/>
  <img alt="Points" title="Points" src="https://custom-icon-badges.demolab.com/badge/Points: 4-1F222E?style=for-the-badge&logoColor=white&logo=award"/>
  <img alt="Average Time" title="Average Time" src="https://custom-icon-badges.demolab.com/badge/Average%20Time: 30m-1F222E?style=for-the-badge&logoColor=white&logo=clock"/>
</p>

## Problem Statement

You are given a sorted array <b>arr[]</b> of unique integers, an integer <b>k</b>, and a target value <b>x</b>. Return exactly <b>k</b> elements from the array closest to <b>x</b>, excluding <b>x</b> if it exists.

An element <b>a</b> is closer to <b>x</b> than <b>b</b> if:

 

- |a - x| < |b - x|, or
- |a - x| == |b - x| and a > b (i.e., prefer the larger element if tied)
 

 

Return the <b>k</b> closest elements in order of closeness.

<b>Examples:</b>

<pre><b>Input: </b>arr[] = [1, 3, 4, 10, 12], k = 2, x = 4
<b>Output:</b> 3 1
<b>Explanation:</b> 4 is excluded, Closest elements to 4 are: 3 (1), 1 (3). So, the 2 closest elements are: 3 1</pre>

<pre><b>Input: </b>arr[] = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56], k = 4, x = 35
<b>Output:</b> 39 30 42 45
<b>Explanation:</b> First closest element to 35 is 39.
Second closest element to 35 is 30.
Third closest element to 35 is 42.
And fourth closest element to 35 is 45.</pre>

<b>Constraints:</b><br>1 ≤ arr.size() ≤ 10<sup>5</sup><br>1 ≤ k ≤ arr.size()<br>1 ≤ x ≤ 10<sup>6</sup><br>1 ≤ arr[i] ≤ 10<sup>6</sup>

## Expected Complexities
- Time Complexity: O(log n + k)
- Auxiliary Space: O(k)

<hr>

### Tags
- **Topic Tags:** `Arrays` `Binary Search` `Algorithms` `STL` `priority-queue`
- **Company Tags:** `Amazon` `OYO Rooms`

### Related Articles
- [Find K Closest Elements Given Value](https://www.geeksforgeeks.org/find-k-closest-elements-given-value/)
